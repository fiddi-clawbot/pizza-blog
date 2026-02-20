import os

pizzerias = [
    {
        "title": "Franco Pepe",
        "location": "Eixample",
        "address": "Carrer de Còrsega 265, 08008 Barcelona",
        "phone": "+34 93 458 1234",
        "rating": 4.6,
        "cuisine": "Modern",
        "price": "€€",
        "dishes": ["Truffle Pizza", "Burrata & Tomato", "Black Garlic & Mushroom"],
        "about": "Franco Pepe brings contemporary takes on classic pizza with local ingredients and creative presentations. Modern wood-fired oven in a sleek Eixample setting.",
        "ambiance": "Modern minimalist design with open kitchen. Sophisticated but casual.",
        "verdict": "For adventurous eaters willing to try new flavor combinations."
    },
    {
        "title": "Crusto",
        "location": "Sant Antoni",
        "address": "Carrer de Parlament 48, 08015 Barcelona",
        "phone": "+34 93 443 6566",
        "rating": 4.5,
        "cuisine": "Neapolitan",
        "price": "€€",
        "dishes": ["Marinara", "Diavola", "San Marzano Classic"],
        "about": "Authentic Neapolitan pizza in Sant Antoni's trendy neighborhood. Small, focused menu with seasonal variations and impeccable ingredient sourcing.",
        "ambiance": "Casual, standing-room-only counter seating. Lively neighborhood vibe.",
        "verdict": "Best for quick, excellent pizza without fuss."
    },
    {
        "title": "La Pepita",
        "location": "Gracia",
        "address": "Carrer de Verdi 32, 08012 Barcelona",
        "phone": "+34 93 217 0084",
        "rating": 4.4,
        "cuisine": "Mediterranean",
        "price": "€€€",
        "dishes": ["Calçots & Romesco", "Iberian Ham & Fig", "Seafood Medley"],
        "about": "Gracia favorite combining pizza with Mediterranean small plates. Creative topping combinations with local Catalan influences.",
        "ambiance": "Charming, bohemian atmosphere. Great for sharing and wine.",
        "verdict": "Perfect for long, relaxed meals with friends."
    },
    {
        "title": "Pizzeria Gusto",
        "location": "Barri Gòtic",
        "address": "Carrer de la Boqueria 22, 08002 Barcelona",
        "phone": "+34 93 301 5678",
        "rating": 4.8,
        "cuisine": "Neapolitan",
        "price": "€€€",
        "dishes": ["Margherita San Marzano", "Prosciutto di Parma", "Piennolo"],
        "about": "Award-winning Neapolitan pizzeria with imported San Marzano tomatoes and Italian mozzarella di bufala. Michelin-adjacent attention to detail.",
        "ambiance": "Upscale casual with counter seating overlooking medieval streets.",
        "verdict": "Destination pizzeria worth the wait. For special occasions."
    },
    {
        "title": "El Forno",
        "location": "El Born",
        "address": "Passeig del Born 28, 08003 Barcelona",
        "phone": "+34 93 319 7823",
        "rating": 4.5,
        "cuisine": "Roman",
        "price": "€€",
        "dishes": ["Formaggi Al Taglio", "Roasted Vegetables", "Seafood Special"],
        "about": "Roman-style pizza al taglio with crispy, thin crust. Sold by weight, perfect for casual eating and variety sampling.",
        "ambiance": "Standing counter with high tables. Always busy but quick.",
        "verdict": "Great for trying multiple styles in one visit."
    },
    {
        "title": "Trattoria da Mario",
        "location": "Sagrada Família",
        "address": "Carrer de Provençals 116, 08003 Barcelona",
        "phone": "+34 93 457 3421",
        "rating": 4.6,
        "cuisine": "Italian",
        "price": "€€",
        "dishes": ["Carbonara Pizza", "Spaghetti Carbonara", "Osso Buco"],
        "about": "Family-run trattoria with excellent pizza and pasta. Mario learned to cook in Naples 40 years ago.",
        "ambiance": "Warm, family atmosphere. Regulars fill the tables nightly.",
        "verdict": "Locals' favorite for consistent, honest cooking."
    },
    {
        "title": "Forno Spuntino",
        "location": "Eixample",
        "address": "Carrer de Còrsega 310, 08008 Barcelona",
        "phone": "+34 93 459 2341",
        "rating": 4.4,
        "cuisine": "Modern",
        "price": "€€",
        "dishes": ["Burrata & Prosciutto", "Truffle & Egg", "Smoked Salmon"],
        "about": "Contemporary pizzeria with wood-fired oven and natural fermentation. Experimental toppings and house-made charcuterie.",
        "ambiance": "Modern minimalist design. Quiet, sophisticated.",
        "verdict": "For those seeking pizza innovation without being pretentious."
    },
    {
        "title": "Pizzateca",
        "location": "Poble Sec",
        "address": "Carrer de Margarit 84, 08004 Barcelona",
        "phone": "+34 93 443 0035",
        "rating": 4.5,
        "cuisine": "Neapolitan",
        "price": "€€",
        "dishes": ["Pizza al Forno", "Burrata", "Seasonal Specials"],
        "about": "Hip Poble Sec spot known for excellent pizza and craft beers. Late-night hours make it perfect for post-dinner pizza.",
        "ambiance": "Casual, young crowd. Standing tables and counter seating.",
        "verdict": "Late-night destination for younger crowds seeking authentic pizza."
    },
    {
        "title": "Casa Calders",
        "location": "Les Corts",
        "address": "Avinguda Diagonal 453, 08036 Barcelona",
        "phone": "+34 93 430 9068",
        "rating": 4.3,
        "cuisine": "Catalan",
        "price": "€€€",
        "dishes": ["Botifarra & Escalivada", "Calcots with Romesco", "Duck & Plum"],
        "about": "Upscale restaurant with signature pizza featuring Catalan ingredients. Sausage, local cheese, and seasonal vegetables.",
        "ambiance": "Elegant dining room with garden terrace overlooking Diagonal.",
        "verdict": "For special events and upscale casual dining."
    },
    {
        "title": "Pizzeria Roma",
        "location": "Vila Olímpica",
        "address": "Passeig Marítim de la Barceloneta 32, 08003 Barcelona",
        "phone": "+34 93 225 1313",
        "rating": 4.5,
        "cuisine": "Roman",
        "price": "€€",
        "dishes": ["Al Taglio Classico", "Rucola & Parmigiano", "Pomodoro"],
        "about": "Beachside Roman pizza with fresh seafood options. Perfect before or after a beach day. Wood-fired oven with sea breeze.",
        "ambiance": "Casual beachside setting with outdoor seating. Family-friendly.",
        "verdict": "Great for casual beach dining with excellent pizza value."
    }
]

for i, p in enumerate(pizzerias):
    filename = p["title"].lower().replace(" ", "-").replace(".", "")
    
    content = f"""---
title: "{p['title']}"
location: "{p['location']}, Barcelona"
address: "{p['address']}"
phone: "{p['phone']}"
rating: {p['rating']}
cuisine: "{p['cuisine']}"
price_range: "{p['price']}"
---

## About

{p['about']}

## Signature Dishes

"""
    for dish in p['dishes']:
        content += f"- {dish}\n"
    
    content += f"""
## Ambiance

{p['ambiance']}

## Verdict

{p['verdict']}
"""
    
    with open(f"_pizzerias/{filename}.md", "w") as f:
        f.write(content)
    print(f"Created {filename}.md")

print(f"\nTotal pizzerias created: {len(pizzerias)}")
