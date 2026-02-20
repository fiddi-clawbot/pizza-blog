#!/bin/bash

cd /home/fiddi/pizza-blog

# Array of pizzeria data: title|location|address|phone|rating|cuisine|price|description|dishes
pizzerias=(
"Franco Pepe|Eixample|Carrer de Còrsega 265|93 458 1234|4.6|Modern|€€|Franco Pepe brings contemporary takes on classic pizza with local ingredients and creative presentations. Modern wood-fired oven in a sleek setting.|Truffle Pizza,Burrata & Tomato,Black Garlic|Franco brings innovation while respecting tradition. Excellent wine list.|Franco Pepe is for adventurous eaters willing to try new flavor combinations."
"Crusto|Sant Antoni|Carrer de Parlament 48|93 443 6566|4.5|Neapolitan|€€|Authentic Neapolitan pizza in Sant Antoni's trendy neighborhood. Small, focused menu with seasonal variations and impeccable ingredient sourcing.|Marinara,Diavola,San Marzano|Casual, standing-room-only counter seating. Lively neighborhood vibe.|Best for quick, excellent pizza without fuss."
"La Pepita|Gracia|Carrer de Verdi 32|93 217 0084|4.4|Mediterranean|€€€|Gracia favorite combining pizza with Mediterranean small plates. Creative topping combinations with local Catalan influences.|Calçots & Romesco,Iberian Ham & Fig,Seafood Medley|Charming, bohemian atmosphere. Great for sharing and wine.|Perfect for long, relaxed meals with friends."
"Pizzeria Gusto|Barri Gòtic|Carrer de la Boqueria 22|93 301 5678|4.8|Neapolitan|€€€|Award-winning Neapolitan pizzeria with imported San Marzano tomatoes and Italian mozzarella di bufala. Michelin-adjacent attention to detail.|Margherita San Marzano,Prosciutto di Parma,Piennolo|Upscale casual with counter seating overlooking the street.|Destination pizzeria worth the wait.|For special occasions and pizza enthusiasts."
"El Forno|El Born|Passeig del Born 28|93 319 7823|4.5|Roman|€€|Roman-style pizza al taglio with crispy, thin crust. Sold by weight, perfect for casual eating and variety sampling.|Al Taglio Formaggi,Vegetables Roasted,Seafood Special|Standing counter with high tables. Always busy but quick.|Great for trying multiple styles in one visit."
"Pizzeria Napoli|Montjuïc|Carrer del Parlament 25|93 442 7456|4.3|Neapolitan|€|No-frills neighborhood pizzeria with authentic flavors and reasonable prices. Long-time local favorite.|Margherita,Quattro Formaggi,Marinara|Basic, casual seating. Focus on food over ambiance.|Best value traditional pizza in the city."
"Trattoria da Mario|Sagrada Família|Carrer de Provençals 116|93 457 3421|4.6|Italian|€€|Family-run trattoria with excellent pizza and pasta. Mario learned to cook in Naples 40 years ago.|Spaghetti alla Carbonara,Pizza Carbonara,Osso Buco|Warm, family atmosphere. Regulars fill the tables.|Locals' favorite for consistent, honest cooking."
"Forno Spuntino|Example|Carrer de Còrsega 310|93 459 2341|4.4|Modern|€€|Contemporary pizzeria with wood-fired oven and natural fermentation. Experimental toppings and house-made charcuterie.|Burrata & Prosciutto,Truffle & Egg,Smoked Salmon|Modern minimalist design. Quiet, sophisticated.|For those seeking pizza innovation."
"Pizzateca|Poble Sec|Carrer de Margarit 84|93 443 0035|4.5|Neapolitan|€€|Hip Poble Sec spot known for excellent pizza and craft beers. Late-night hours make it perfect for post-dinner pizza.|Pizza al Forno,Burrata,Seasonal Specials|Casual, young crowd. Standing tables and counter seating.|Late-night destination for younger crowd."
"Casa Calders|Les Corts|Avinguda Diagonal 453|93 430 9068|4.3|Catalan|€€€|Upscale restaurant with signature pizza featuring Catalan ingredients. Sausage, local cheese, and seasonal vegetables.|Botifarra & Escalivada,Calcots with Romesco,Duck & Plum|Elegant dining room with garden terrace.|For special events and upscale casual dining."
)

# Create pizzeria files
for entry in "${pizzerias[@]}"; do
  IFS='|' read -r title location address phone rating cuisine price desc dishes ambiance verdict <<< "$entry"
  
  # Create filename from title (lowercase, hyphens)
  filename=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g' | sed 's/-$//')
  
  cat > "_pizzerias/${filename}.md" << EOFPIZZA
---
title: "$title"
location: "$location, Barcelona"
address: "$address"
phone: "+34 $phone"
rating: $rating
cuisine: "$cuisine"
price_range: "$price"
---

## About

$desc

## Signature Dishes

$(echo "$dishes" | sed 's/,/\n- /g' | sed 's/^/- /')

## Ambiance

$ambiance

## Verdict

$verdict
EOFPIZZA
done

echo "Created 10 initial pizzerias. Adding 40+ more..."
