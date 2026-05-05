#!/usr/bin/env python3
"""
Lyra Prompts — Sub-Kategorisierungs-Skript

Teilt grosse Hauptkategorien in thematische Unterordner auf, schreibt das
`unterkategorie:`-Feld im Frontmatter und macht aus dem Bibliothek-Chaos
echte Regale + Faecher.

Usage:
  python3 sort-subcategories.py --dry-run
  python3 sort-subcategories.py --execute
"""

import re
import sys
import shutil
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent / "kategorien"

# ─── TAXONOMIE PRO HAUPTKATEGORIE ─────────────────────────────────────
# Jede Unterkategorie: (folder, display_name, strong_words, keywords)
# strong: +5 pro Treffer, keywords: +2 pro Treffer
# Reihenfolge ist Prioritaet bei Score-Gleichstand.

TAXONOMY = {
    "bildbearbeitung-visualisierung": [
        (
            "portraits-menschen", "Portraits & Menschen",
            ["portrait", "headshot", "self-portrait", "face of", "facial",
             "candid portrait", "studio portrait"],
            ["man", "woman", "girl", "boy", "child", "kid", "baby", "teenage",
             "elderly", "person", "people", "human", "model wearing",
             "lady", "gentleman", "bearded", "smiling"],
        ),
        (
            "fashion-beauty", "Fashion & Beauty",
            ["fashion photography", "high fashion", "haute couture",
             "beauty shot", "glamour shot", "vogue", "editorial fashion",
             "runway", "makeup artist style"],
            ["fashion", "beauty", "glamor", "glamour", "couture", "wearing",
             "outfit", "lipstick", "eyeshadow", "model pose", "boutique",
             "lookbook", "stylist"],
        ),
        (
            "fotografie-stile", "Fotografie-Stile",
            ["polaroid", "analog photography", "large format", "medium format",
             "35mm film", "kodak portra", "fuji film", "lomography",
             "paparazzi shot", "lifestyle photography", "documentary photo",
             "street photography", "long exposure", "tilt shift",
             "double exposure", "pictorialism"],
            ["photo", "photography", "photograph", "shutter", "aperture",
             "iso", "bokeh", "lens", "zoom", "wide angle", "telephoto",
             "macro", "lighting", "softbox", "golden hour", "blue hour",
             "cinematic", "film grain"],
        ),
        (
            "3d-render-isometric", "3D-Render & Isometric",
            ["isometric", "3d render", "octane render", "blender render",
             "unreal engine", "voxel art", "low poly", "diorama",
             "exploded view", "claymation", "miniature scene",
             "3d model", "cgi", "ray traced"],
            ["3d", "render", "diorama", "miniature", "isometry", "voxel",
             "polygon", "ray tracing", "subsurface scattering", "pbr texture"],
        ),
        (
            "illustration-malerei", "Illustration & Malerei",
            ["watercolor", "oil painting", "gouache", "acrylic painting",
             "ink illustration", "pencil sketch", "charcoal drawing",
             "botanical illustration", "vintage illustration",
             "art nouveau", "art deco", "ukiyo-e", "block print",
             "anime style", "manga style", "cartoon style", "comic style",
             "marvel comics", "dc comics", "graphic novel"],
            ["illustration", "painting", "drawing", "sketch", "doodle",
             "watercolour", "ink wash", "etching", "lithograph",
             "anime", "manga", "cartoon", "comic", "vector art",
             "flat illustration"],
        ),
        (
            "landschaft-architektur", "Landschaft & Architektur",
            ["landscape photography", "cityscape", "skyline", "aerial view",
             "drone shot", "architectural photography", "interior design",
             "urban photography", "street view", "panorama"],
            ["landscape", "mountain", "forest", "ocean", "desert", "sunset",
             "sunrise", "city", "urban", "skyline", "building", "architecture",
             "interior", "room", "living room", "kitchen design",
             "panorama", "vista", "horizon"],
        ),
        (
            "fantasy-scifi-konzept", "Fantasy, Sci-Fi & Konzept",
            ["concept art", "fantasy art", "sci-fi art", "cyberpunk",
             "steampunk", "dystopian", "post-apocalyptic", "alien world",
             "space opera", "magical realism", "dark fantasy",
             "creature design", "character concept"],
            ["fantasy", "sci-fi", "scifi", "cyberpunk", "steampunk",
             "dystopia", "alien", "spaceship", "dragon", "wizard", "magic",
             "mythical", "creature", "monster", "futuristic", "neon",
             "surreal", "dreamscape"],
        ),
        (
            "produkt-werbung", "Produkt & Werbung",
            ["product shot", "product photography", "commercial photo",
             "advertisement", "ad campaign", "packaging design",
             "mockup", "brand identity", "logo design", "poster design",
             "billboard"],
            ["product", "commercial", "advertising", "advertisement",
             "packaging", "mockup", "branding", "logo", "poster",
             "flyer", "billboard"],
        ),
        (
            "abstrakt-pattern", "Abstrakt & Pattern",
            ["abstract art", "abstract pattern", "geometric pattern",
             "fractal art", "generative art", "kaleidoscope",
             "minimalist design", "bauhaus", "color field"],
            ["abstract", "pattern", "geometric", "fractal", "generative",
             "kaleidoscope", "minimalist", "minimalism", "texture",
             "wallpaper", "tile pattern"],
        ),
        (
            "prompt-werkzeuge", "Prompt-Werkzeuge",
            ["midjourney prompt generator", "stable diffusion prompt",
             "sdxl prompt", "dall-e prompt generator", "flux prompt",
             "prompt engineer for image"],
            ["prompt generator", "prompt builder", "prompt template",
             "negative prompt"],
        ),
    ],

    "technik-alltag": [
        (
            "programmiersprachen", "Programmiersprachen",
            ["python expert", "javascript expert", "typescript expert",
             "rust developer", "golang developer", "c++ developer",
             "java developer", "ruby on rails", "swift developer",
             "kotlin developer", "php developer"],
            ["python", "javascript", "typescript", "rust", "golang",
             "c++", "java ", "ruby", "swift", "kotlin", "php", "perl",
             "scala", "haskell", "lua", "elixir", "clojure"],
        ),
        (
            "web-app-entwicklung", "Web- & App-Entwicklung",
            ["web developer", "frontend developer", "backend developer",
             "fullstack developer", "react developer", "vue developer",
             "angular developer", "next.js", "nuxt.js", "ux ui developer",
             "web design consultant", "mobile app developer",
             "ios developer", "android developer", "flutter developer",
             "react native", "tailwind css"],
            ["html", "css", "react", "vue", "angular", "svelte",
             "next.js", "nuxt", "frontend", "backend", "fullstack",
             "web app", "mobile app", "responsive design", "tailwind",
             "ui component", "ux design", "single page application"],
        ),
        (
            "ki-agenten-llm", "KI, Agenten & LLM",
            ["llm", "large language model", "ai agent", "autonomous agent",
             "prompt engineer", "chatbot developer", "rag system",
             "vector database", "fine-tuning", "machine learning engineer",
             "deep learning", "neural network", "transformer architecture",
             "computer vision engineer", "nlp engineer"],
            ["ai", "llm", "agent", "chatbot", "embedding", "rag",
             "fine-tune", "machine learning", "deep learning", "neural",
             "transformer", "computer vision", "nlp ", "tensorflow",
             "pytorch", "huggingface", "openai", "anthropic"],
        ),
        (
            "daten-datenbanken-sql", "Daten, Datenbanken & SQL",
            ["sql query generator", "database administrator",
             "data engineer", "data analyst", "data scientist",
             "etl pipeline", "data warehouse", "business intelligence",
             "tableau expert", "power bi"],
            ["sql", "nosql", "database", "postgres", "postgresql", "mysql",
             "mongodb", "redis", "elasticsearch", "snowflake", "bigquery",
             "data pipeline", "etl", "data warehouse", "dataset", "csv",
             "spreadsheet", "excel sheet", "tableau", "power bi"],
        ),
        (
            "devops-cloud-infra", "DevOps, Cloud & Infrastruktur",
            ["devops engineer", "site reliability engineer", "cloud architect",
             "kubernetes administrator", "docker expert", "ci/cd pipeline",
             "terraform", "ansible playbook", "aws solutions architect",
             "azure architect", "gcp architect"],
            ["devops", "kubernetes", "docker", "container", "terraform",
             "ansible", "ci/cd", "aws", "azure", "gcp", "cloud",
             "infrastructure", "deploy", "deployment", "serverless",
             "lambda", "monitoring", "observability", "prometheus", "grafana"],
        ),
        (
            "security-hacking-blockchain", "Security, Hacking & Blockchain",
            ["cyber security specialist", "ethical hacker", "penetration tester",
             "security analyst", "blockchain developer", "smart contract",
             "solidity developer", "ethereum developer", "web3 expert"],
            ["cyber security", "cybersecurity", "penetration", "pentest",
             "vulnerability", "exploit", "encryption", "cryptography",
             "blockchain", "ethereum", "solidity", "smart contract", "web3",
             "nft", "wallet", "crypto"],
        ),
        (
            "automation-scripting-cli", "Automation, Scripting & CLI",
            ["bash script", "shell script", "powershell script",
             "linux terminal", "regex", "regular expression",
             "automation engineer", "rpa developer", "scraping expert",
             "browser automation"],
            ["bash", "shell", "powershell", "terminal", "command line",
             "cli", "regex", "automation", "scrape", "scraping", "crawler",
             "webhook", "cron", "script"],
        ),
        (
            "system-architektur-engineering", "System-Architektur & Engineering",
            ["system architect", "software architect", "solutions architect",
             "principal engineer", "tech lead", "engineering manager",
             "code reviewer", "code refactorer", "performance engineer",
             "api designer", "microservices architect"],
            ["architecture", "architect", "design pattern", "microservice",
             "monolith", "api design", "rest api", "graphql", "grpc",
             "code review", "refactor", "performance optimization",
             "scalability", "concurrency"],
        ),
    ],

    "lernen-wachstum": [
        (
            "sprachen-uebersetzen", "Sprachen & Uebersetzen",
            ["language tutor", "translator", "translation expert",
             "english tutor", "german tutor", "chinese translator",
             "spanish tutor", "french tutor", "grammar coach",
             "vocabulary trainer", "writing coach"],
            ["language", "translate", "translation", "grammar", "vocabulary",
             "tutor", "english", "german", "spanish", "french", "chinese",
             "japanese", "italian", "linguistic", "pronunciation"],
        ),
        (
            "mathe-naturwissenschaft", "Mathe & Naturwissenschaft",
            ["math teacher", "mathematician", "physics tutor",
             "chemistry tutor", "biology tutor", "statistics expert",
             "data scientist tutor"],
            ["math", "mathematics", "algebra", "geometry", "calculus",
             "statistics", "physics", "chemistry", "biology", "scientific"],
        ),
        (
            "geschichte-philosophie", "Geschichte & Philosophie",
            ["historian", "philosopher", "philosophy teacher",
             "ethics professor", "history teacher", "social science"],
            ["history", "historian", "philosophy", "philosophical",
             "ethics", "ethical", "moral", "sociology", "anthropology",
             "political science"],
        ),
        (
            "ki-prompt-engineering", "KI- & Prompt-Engineering",
            ["prompt generator for language", "prompt engineer", "llm tutor",
             "ai prompt designer", "chatgpt prompt expert"],
            ["prompt generator", "prompt template", "llm", "ai model",
             "chatgpt", "gemini", "claude", "anthropic", "openai prompt"],
        ),
        (
            "lerncoaching-paedagogik", "Lerncoaching & Paedagogik",
            ["learning coach", "study coach", "academic advisor",
             "exam prep coach", "homework helper", "curriculum designer",
             "school life mentor", "tutor for students"],
            ["learning", "study", "exam", "homework", "curriculum",
             "education", "pedagogy", "classroom", "student", "school",
             "university", "college", "academic"],
        ),
    ],

    "kreativitaet-freizeit": [
        (
            "schreiben-poesie", "Schreiben & Poesie",
            ["novelist", "screenwriter", "poet", "ghostwriter",
             "creative writing coach", "storyteller", "playwright",
             "essay writer"],
            ["story", "novel", "poem", "poetry", "screenplay", "screenwrit",
             "narrative", "fiction", "non-fiction", "essay", "memoir",
             "short story", "haiku", "verse"],
        ),
        (
            "musik-comedy-buehne", "Musik, Comedy & Buehne",
            ["composer", "songwriter", "rapper", "music producer",
             "stand-up comedian", "comedy writer", "voice actor",
             "magician", "theater director"],
            ["music", "song", "rap ", "lyrics", "melody", "composition",
             "comedy", "joke", "stand-up", "improv", "theater", "stage",
             "monologue", "magician"],
        ),
        (
            "spiele-quiz-raetsel", "Spiele, Quiz & Raetsel",
            ["text adventure game", "quiz master", "trivia generator",
             "puzzle designer", "game master", "rpg dungeon master",
             "board game designer", "riddle creator"],
            ["game", "quiz", "trivia", "puzzle", "riddle", "rpg",
             "dungeon master", "board game", "card game", "tabletop"],
        ),
        (
            "film-medien-kritik", "Film, Medien & Kritik",
            ["film critic", "movie critic", "tv critic", "video essayist",
             "documentary maker", "youtube scriptwriter", "podcast host",
             "video editor", "cinematic director"],
            ["movie", "film", "cinema", "documentary", "tv series",
             "podcast", "youtube", "video essay", "vlog", "broadcaster"],
        ),
        (
            "diy-hobby-handwerk", "DIY, Hobby & Handwerk",
            ["interior decorator", "florist", "diy expert",
             "knitting expert", "woodworking", "home improvement",
             "crafting tutor", "lego designer"],
            ["diy", "hobby", "basteln", "knitting", "crochet",
             "woodworking", "lego", "origami", "decoration", "florist",
             "scrapbook"],
        ),
    ],

    "alltag-leben": [
        (
            "kochen-essen-rezepte", "Kochen, Essen & Rezepte",
            ["chef", "personal chef", "recipe finder", "food critic",
             "meal prep", "pastry chef", "barista", "sommelier",
             "ayurveda food"],
            ["recipe", "rezept", "cook", "kochen", "backen", "baking",
             "kitchen", "kueche", "meal", "food", "essen", "ingredient",
             "zutaten", "diet plan", "menu", "restaurant"],
        ),
        (
            "haushalt-organisation", "Haushalt & Organisation",
            ["personal organizer", "decluttering coach", "cleaning planner",
             "household manager", "moving planner"],
            ["haushalt", "household", "putzen", "cleaning", "tidying",
             "wohnung", "umzug", "moving", "organisation", "routine",
             "checklist", "putzplan", "miete", "rent"],
        ),
        (
            "familie-kinder-haustiere", "Familie, Kinder & Haustiere",
            ["babysitter", "pet behaviorist", "parenting coach",
             "children's book creator", "family mediator"],
            ["kinder", "kid", "baby", "child", "parent", "eltern",
             "familie", "family", "haustier", "pet", "hund", "dog",
             "katze", "cat", "animal"],
        ),
        (
            "reisen-transport", "Reisen & Transport",
            ["travel guide", "travel planner", "cheap travel ticket",
             "automobile mechanic", "car navigation system",
             "real estate agent for travel"],
            ["travel", "reise", "urlaub", "vacation", "trip", "flight",
             "hotel", "auto", "car", "fahrzeug", "vehicle", "navigation",
             "roadtrip"],
        ),
        (
            "wohnen-immobilien-finanzen", "Wohnen, Immobilien & Finanzen",
            ["real estate agent", "personal finance coach", "budget tracker",
             "tax assistant", "investment manager for daily"],
            ["budget", "finanzen", "finance", "geld", "money", "saving",
             "schulden", "debt", "miete", "rent", "immobilie", "real estate",
             "wohnen", "moving cost"],
        ),
        (
            "shopping-mode-stil", "Shopping, Mode & Stil",
            ["personal shopper", "personal stylist", "makeup artist",
             "fashion advisor for everyday"],
            ["shopping", "einkauf", "kleidung", "outfit", "stylist",
             "shopper", "wardrobe", "garderobe"],
        ),
        (
            "garten-pflanzen", "Garten & Pflanzen",
            ["gardener", "florist for home", "plant care expert"],
            ["garten", "garden", "pflanze", "plant", "blume", "flower",
             "vegetable garden", "balkon", "hydroponic"],
        ),
    ],

    "beruf-karriere": [
        (
            "bewerbung-job-suche", "Bewerbung & Job-Suche",
            ["job interviewer", "recruiter", "career coach for resume",
             "cover letter expert", "resume writer", "linkedin profile"],
            ["bewerbung", "lebenslauf", "resume", "cv ", "cover letter",
             "anschreiben", "interview", "vorstellungsgespraech", "vorstellungsgespräch",
             "recruiter", "hire", "linkedin profile", "job application"],
        ),
        (
            "fuehrung-management", "Fuehrung & Management",
            ["chief executive officer", "ceo coach", "team lead coach",
             "engineering manager", "product manager", "project manager",
             "executive briefing"],
            ["leadership", "fuehrung", "führung", "management", "manager",
             "executive", "ceo", "cto", "cfo", "team lead", "supervisor",
             "delegation"],
        ),
        (
            "verkauf-marketing-pitch", "Verkauf, Marketing & Pitch",
            ["sales coach", "pitch coach", "marketing strategist",
             "salesperson", "negotiation coach for sales"],
            ["sales", "verkauf", "pitch", "marketing strategy",
             "lead generation", "funnel", "cold email", "outreach",
             "negotiation"],
        ),
        (
            "unternehmensgruendung-strategie", "Unternehmensgruendung & Strategie",
            ["startup mentor", "business plan writer", "founder coach",
             "business strategist", "venture capitalist advisor"],
            ["startup", "gruendung", "gründung", "founder", "business plan",
             "geschaeftsplan", "geschäftsplan", "business strategy",
             "investor", "vc ", "fundraising"],
        ),
        (
            "freelance-selbststaendig", "Freelance & Selbststaendig",
            ["freelancer coach", "consultant for solopreneur",
             "self-employed advisor"],
            ["freelancer", "freelance", "selbststaendig", "selbständig",
             "solopreneur", "consultant", "side hustle", "kleinunternehmer"],
        ),
        (
            "recht-finanzen-buchhaltung", "Recht, Finanzen & Buchhaltung",
            ["accountant", "financial analyst", "investment manager",
             "startup tech lawyer", "tax advisor"],
            ["accountant", "buchhaltung", "tax", "steuer", "rechnung",
             "financial analyst", "compliance", "audit"],
        ),
        (
            "produktivitaet-arbeitsweise", "Produktivitaet & Arbeitsweise",
            ["time management coach", "productivity coach",
             "logistician", "talent coach"],
            ["productivity", "produktivitaet", "produktivität", "time management",
             "deep work", "kanban", "agile", "scrum", "okr",
             "performance review"],
        ),
    ],

    "gesundheit-wohlbefinden": [
        (
            "fitness-bewegung", "Fitness & Bewegung",
            ["personal trainer", "virtual fitness coach",
             "remote worker fitness trainer", "yoga teacher",
             "running coach", "strength coach"],
            ["fitness", "workout", "training", "exercise", "gym",
             "running", "laufen", "yoga", "pilates", "calisthenics",
             "muscle", "strength", "cardio"],
        ),
        (
            "ernaehrung-diaet", "Ernaehrung & Diaet",
            ["nutritionist", "dietitian", "meal plan coach",
             "weight loss specialist"],
            ["nutrition", "ernaehrung", "ernährung", "diet", "diaet", "diät",
             "abnehmen", "weight loss", "calorie", "kalorien", "macro",
             "protein"],
        ),
        (
            "mental-health-psyche", "Mental Health & Psyche",
            ["mental health adviser", "psychologist", "therapist",
             "burnout coach", "stress coach", "trauma therapist"],
            ["mental health", "psyche", "psycholog", "therapie", "therapy",
             "stress", "burnout", "anxiety", "depression", "achtsamkeit",
             "mindfulness", "meditation"],
        ),
        (
            "schlaf-erholung", "Schlaf & Erholung",
            ["sleep coach", "insomnia therapist", "recovery specialist"],
            ["schlaf", "sleep", "insomnia", "ruhe", "erholung", "recovery",
             "nap", "circadian"],
        ),
        (
            "medizin-arzt-symptome", "Medizin, Arzt & Symptome",
            ["virtual doctor", "ai-assisted doctor", "dentist",
             "medical consultant", "diabetes treatment advisor",
             "health metrics calculator", "healing grandma"],
            ["doctor", "arzt", "dentist", "zahnarzt", "symptom",
             "krankheit", "disease", "diagnose", "diagnosis", "treatment",
             "medikament", "medicine", "blood pressure", "diabetes"],
        ),
        (
            "selbstfuersorge-ritual", "Selbstfuersorge & Ritual",
            ["self-care coach", "ayurveda food tester", "wellness guide",
             "spa ritual designer"],
            ["self-care", "selbstfuersorge", "selbstfürsorge", "wellness",
             "ritual", "spa", "ayurveda", "skincare", "hautpflege"],
        ),
    ],

    "kommunikation-beziehungen": [
        (
            "beziehung-partnerschaft", "Beziehung & Partnerschaft",
            ["relationship coach", "couples counselor", "dating coach",
             "marriage advisor"],
            ["beziehung", "relationship", "partner", "ehe", "marriage",
             "dating", "couple", "konflikt", "trennung", "breakup"],
        ),
        (
            "rhetorik-praesentation-debatte", "Rhetorik, Praesentation & Debatte",
            ["debater", "debate coach", "public speaking coach",
             "elocutionist", "motivational speaker", "rhetoric expert",
             "presentation coach"],
            ["rhetorik", "rhetoric", "debate", "speech", "elocution",
             "public speaking", "presentation", "pitch deck",
             "ueberzeugen", "persuasion", "storytelling"],
        ),
        (
            "social-media-content", "Social Media & Content",
            ["social media manager", "social media influencer",
             "content creator", "tiktok strategist", "instagram strategist",
             "linkedin content"],
            ["social media", "instagram", "tiktok", "linkedin", "twitter",
             "youtube channel", "creator", "influencer", "viral",
             "engagement", "hashtag"],
        ),
        (
            "marketing-werbung-pr", "Marketing, Werbung & PR",
            ["advertiser", "branding strategist", "seo specialist",
             "ghostwriter", "pr expert", "copywriter"],
            ["marketing", "werbung", "advertising", "branding", "seo",
             "copywriting", "newsletter", "campaign", "public relations"],
        ),
        (
            "konflikt-feedback-mediation", "Konflikt, Feedback & Mediation",
            ["conflict mediator", "feedback coach",
             "coach for identifying growth", "negotiation coach"],
            ["conflict", "konflikt", "mediation", "feedback",
             "negotiation", "verhandlung", "dispute", "boundary"],
        ),
        (
            "schreiben-emails-briefe", "Schreiben (E-Mails & Briefe)",
            ["email writer", "letter writer", "ghostwriter for emails"],
            ["email", "e-mail", "brief", "letter", "memo", "nachricht",
             "message", "smalltalk", "chitchat"],
        ),
        (
            "journalismus-medien", "Journalismus & Medien",
            ["journalist", "commentariat", "editor in chief",
             "fact checker"],
            ["journalist", "newsroom", "reporter", "editorial",
             "fact check", "kommentariat", "media analyst"],
        ),
    ],

    "spezielle-situationen": [
        (
            "recht-anwalt-vertrag", "Recht, Anwalt & Vertrag",
            ["legal advisor", "lawyer", "judicial advisor",
             "trade contract review", "tax and commercial expert",
             "business legal assistant", "china business law"],
            ["legal", "law", "lawyer", "anwalt", "kanzlei", "court",
             "gericht", "vertrag", "contract", "compliance", "klage",
             "klausel"],
        ),
        (
            "krise-notfall-erste-hilfe", "Krise, Notfall & Erste Hilfe",
            ["emergency response professional", "crisis counselor",
             "first aid expert"],
            ["emergency", "notfall", "krise", "crisis", "first aid",
             "erste hilfe", "evacuation", "disaster"],
        ),
        (
            "trauer-trennung-lebenswenden", "Trauer, Trennung & Lebenswenden",
            ["grief counselor", "divorce mediator",
             "buddhist monk who just lost"],
            ["grief", "trauer", "todesfall", "verlust", "scheidung",
             "divorce", "separation"],
        ),
        (
            "behoerden-immigration-versicherung", "Behoerden, Immigration & Versicherung",
            ["immigration consultant", "visa expert", "insurance advisor"],
            ["immigration", "auswandern", "visa", "asyl", "behoerde",
             "behörde", "versicherung", "insurance", "claim"],
        ),
        (
            "ethik-osint-analyse", "Ethik, OSINT & Analyse",
            ["fallacy finder", "source hunting osint mode",
             "swot analysis political risk", "corporate intel report",
             "historian"],
            ["fallacy", "osint", "open source intelligence", "swot",
             "intelligence report", "ethics", "ethik", "moral dilemma"],
        ),
        (
            "spezialprojekte", "Spezialprojekte",
            ["camp planner", "media center plan for hajj",
             "graduate information project", "act as if you are a buddhist"],
            ["camp planner", "hajj", "graduate", "ceremony",
             "special event", "ritual planning"],
        ),
    ],

    "pro": [
        (
            "webentwicklung-pwa", "Webentwicklung & PWA",
            ["pwa booking", "pwa finance", "pwa fitness",
             "pwa ki crm", "pwa projekt board", "pwa rezept",
             "pwa telemedizin", "pwa vorrats", "global news scraper"],
            ["pwa", "progressive web app", "react app", "next.js",
             "dashboard", "crm"],
        ),
        (
            "business-strategie", "Business & Strategie",
            ["business-strategie", "executive briefing",
             "ki-system architektur", "weltanalyse"],
            ["business strategy", "executive briefing", "system architektur",
             "weltanalyse"],
        ),
        (
            "coaching-personal", "Coaching (Personal)",
            ["bewerbung-traumjob", "beziehung-konfliktloeser",
             "prokrastination-vernichter", "schlafprobleme-loesen",
             "schuldenfrei-finanzplan"],
            ["traumjob", "konfliktloeser", "prokrastination",
             "schlafprobleme", "schuldenfrei"],
        ),
        (
            "marketing-content", "Marketing & Content",
            ["instagram-aufbau", "finanzmodell-erstellen"],
            ["instagram aufbau", "finanzmodell"],
        ),
    ],
}


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None


def parse_frontmatter(content):
    """Liefert (fm_dict, full_text_lower) fuer Scoring."""
    fm = {}
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            mm = re.match(r"^([^:]+):\s*(.+)$", line)
            if mm:
                key = mm.group(1).strip()
                val = mm.group(2).strip().strip('"').strip("'")
                fm[key] = val
    title = fm.get("titel", "")
    tags = fm.get("tags", "")
    body = content[m.end():] if m else content
    return fm, f"{title} {tags} {body}".lower()


def score_subcat(text, strong, keywords):
    score = 0
    for w in strong:
        if w.lower() in text:
            score += 5
    for w in keywords:
        if w.lower() in text:
            score += 2
    return score


def best_subcategory(text, subcats):
    """Liefert (folder, display, score) der besten Unterkategorie."""
    best = (None, None, 0)
    for folder, display, strong, keywords in subcats:
        s = score_subcat(text, strong, keywords)
        if s > best[2]:
            best = (folder, display, s)
    return best


def update_unterkategorie(content, new_value):
    """Setzt oder ergaenzt das `unterkategorie:`-Feld im Frontmatter."""
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return content
    fm_block = m.group(1)
    new_line = f'unterkategorie: "{new_value}"'
    if re.search(r"^unterkategorie:\s*.*$", fm_block, re.MULTILINE):
        new_fm = re.sub(
            r"^unterkategorie:\s*.*$", new_line, fm_block, count=1,
            flags=re.MULTILINE,
        )
    else:
        new_fm = fm_block + "\n" + new_line
    return content.replace(m.group(0), f"---\n{new_fm}\n---", 1)


def analyze():
    """Liefert Liste (filepath, main, sub_folder, sub_display, score)."""
    moves = []
    unmatched = []

    for main_cat, subcats in TAXONOMY.items():
        cat_dir = BASE / main_cat
        if not cat_dir.exists():
            continue
        for md in sorted(cat_dir.glob("*.md")):
            content = read_file(md)
            if content is None:
                continue
            _, text = parse_frontmatter(content)
            folder, display, score = best_subcategory(text, subcats)
            if folder is None or score < 2:
                unmatched.append((md, main_cat))
            else:
                moves.append((md, main_cat, folder, display, score))
    return moves, unmatched


def print_report(moves, unmatched):
    by_main = defaultdict(lambda: defaultdict(int))
    for _, main, sub, _, _ in moves:
        by_main[main][sub] += 1
    print("=" * 70)
    print("  SUB-KATEGORISIERUNG — REPORT")
    print("=" * 70)
    for main in sorted(by_main):
        print(f"\n  {main}:")
        for sub in sorted(by_main[main], key=lambda s: -by_main[main][s]):
            print(f"    {sub:<35} {by_main[main][sub]:>5}")
        unmatched_count = sum(1 for _, m in unmatched if m == main)
        if unmatched_count:
            print(f"    {'_sonstiges':<35} {unmatched_count:>5}")
    print(f"\n  Gesamt einsortierbar: {len(moves)}")
    print(f"  Unklar (-> _sonstiges): {len(unmatched)}\n")


def execute(moves, unmatched):
    moved = 0
    failed = 0

    # Klare Treffer
    for md, main, sub, display, _ in moves:
        target_dir = BASE / main / sub
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / md.name
        if target.exists():
            target = target_dir / f"{md.stem}-2{md.suffix}"

        try:
            content = read_file(md)
            new_content = update_unterkategorie(content, display)
            with open(md, "w", encoding="utf-8") as f:
                f.write(new_content)
            shutil.move(str(md), str(target))
            moved += 1
        except Exception as e:
            print(f"  FEHLER {md.name}: {e}")
            failed += 1

    # Unklare in _sonstiges
    for md, main in unmatched:
        target_dir = BASE / main / "_sonstiges"
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / md.name
        if target.exists():
            target = target_dir / f"{md.stem}-2{md.suffix}"
        try:
            content = read_file(md)
            new_content = update_unterkategorie(content, "Sonstiges")
            with open(md, "w", encoding="utf-8") as f:
                f.write(new_content)
            shutil.move(str(md), str(target))
            moved += 1
        except Exception as e:
            print(f"  FEHLER {md.name}: {e}")
            failed += 1

    print(f"\n  Verschoben: {moved}")
    print(f"  Fehler:     {failed}\n")


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--dry-run", "--execute"):
        print("Usage:")
        print("  python3 sort-subcategories.py --dry-run")
        print("  python3 sort-subcategories.py --execute")
        sys.exit(1)

    moves, unmatched = analyze()
    print_report(moves, unmatched)

    if sys.argv[1] == "--execute":
        execute(moves, unmatched)


if __name__ == "__main__":
    main()
