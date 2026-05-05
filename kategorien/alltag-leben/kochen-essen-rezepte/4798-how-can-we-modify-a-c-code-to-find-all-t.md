---
id: "#4798"
titel: "How can we modify a C# code to find all the recipes that use"
kategorie: "Alltag & Leben"
unterkategorie: "Kochen, Essen & Rezepte"
tags: ["modify", "code", "find", "recipes", "ingredients"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "openrlhf-UltraFeedback"
erstellt: "2026-04-29"
---

## Prompt

```
How can we modify a C# code to find all the recipes that use ingredients exclusively found in high altitude regions? Here is a sample code that you can use as a reference:
List<string> highAltitudeIngredients = new List<string>() { "quinoa", "maca", "chuño", "potatoes", "alpaca meat", "llama meat", "peanuts", "corn", "amaranth" };
List<Recipe> highAltitudeRecipes = new List<Recipe>();
foreach (Recipe recipe in allRecipes)
{
   bool isHighAltitudeRecipe = true;
   foreach (Ingredient ingredient in recipe.Ingredients)
   {
      if (!highAltitudeIngredients.Contains(ingredient.Name.ToLower()))
      {
         isHighAltitudeRecipe = false;
         break;
      }
   }
   if (isHighAltitudeRecipe)
   {
      highAltitudeRecipes.Add(recipe);
   }
}
return highAltitudeRecipes;
```

## Anwendung

**Thema: How Can, Find All** — Perfekt fuer alle, die neue Rezeptideen suchen oder ihre Kochkuenste erweitern wollen. Die KI erstellt ein vollstaendiges Rezept mit Zutaten und Anleitung.

Kopiere den Prompt und fuege ihn in ChatGPT, Claude oder Gemini ein.
Passe die Details an deine Beduerfnisse an.

## Variationen

- Ersetze Zutaten durch das, was du im Kuehlschrank hast
- Fuege "fuer [X] Personen" hinzu fuer angepasste Mengen
- Frage nach einer veganen/vegetarischen Alternative
- Bitte um Naehrwertangaben pro Portion
