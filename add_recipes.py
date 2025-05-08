from recipes_data import recipes

recipes = [
    {
        "id": 1,
        "name": "Paneer Butter Masala",
        "image_url": "/static/images/paneer_butter_masala.jpg",
        "category": "Vegetarian",
        "ingredients": [
            "250g paneer (cubed)",
            "2 tbsp butter",
            "1 onion (chopped)",
            "2 tomatoes (pureed)",
            "1 tsp ginger garlic paste",
            "1/2 cup cream",
            "Spices: garam masala, red chili powder, turmeric, salt"
        ],
        "steps": [
            "Heat butter in a pan, sauté onions until golden.",
            "Add ginger garlic paste and cook for 2 mins.",
            "Pour in tomato puree, cook till oil separates.",
            "Add spices and mix well.",
            "Add paneer cubes and cook for 5-7 mins.",
            "Stir in cream, simmer for 2 mins and serve hot."
        ]
    },
    {
        "id": 2,
        "name": "Veg Biryani",
        "image_url": "/static/images/veg_biryani.jpg",
        "category": "Vegetarian",
        "ingredients": [
            "1 cup basmati rice",
            "1/2 cup mixed vegetables",
            "1 onion (sliced)",
            "2 tbsp curd",
            "Biryani masala, saffron, mint leaves, coriander"
        ],
        "steps": [
            "Cook rice till 90% done.",
            "Sauté onions and veggies in oil.",
            "Add curd, spices and mix well.",
            "Layer rice and veggie masala, add saffron water.",
            "Cover and cook on low heat for 15 mins."
        ]
    },
    {
        "id": 3,
        "name": "Chole Masala",
        "image_url": "/static/images/chole.jpg",
        "category": "Vegetarian",
        "ingredients": [
            "1 cup boiled chickpeas",
            "1 onion, 1 tomato, ginger garlic paste",
            "Chole masala, turmeric, red chili powder"
        ],
        "steps": [
            "Sauté onions, add ginger garlic paste.",
            "Add tomato puree and spices.",
            "Mix in chickpeas and cook 10-15 mins.",
            "Garnish with coriander and serve."
        ]
    },
    {
        "id": 4,
        "name": "Vegetable Pulao",
        "image_url": "/static/images/veg_pulao.jpg",
        "category": "Vegetarian",
        "ingredients": [
            "1 cup basmati rice",
            "1 cup mixed vegetables",
            "Whole spices (clove, cardamom, bay leaf)",
            "Ginger, garlic, green chili"
        ],
        "steps": [
            "Sauté whole spices, ginger and garlic.",
            "Add vegetables and sauté 2-3 mins.",
            "Add rice and water, cook till done.",
            "Serve hot with raita."
        ]
    },
    {
        "id": 5,
        "name": "Palak Paneer",
        "image_url": "/static/images/palak_paneer.jpg",
        "category": "Vegetarian",
        "ingredients": [
            "200g paneer cubes",
            "1 bunch spinach (pureed)",
            "1 onion, tomato, ginger garlic paste",
            "Spices: cumin, garam masala, salt"
        ],
        "steps": [
            "Blanch spinach and blend.",
            "Sauté onions and tomato with spices.",
            "Add spinach puree and simmer.",
            "Add paneer cubes and cook 5 mins."
        ]
    },

    # ----------- Non-Vegetarian ----------- #
    {
        "id": 6,
        "name": "Butter Chicken",
        "image_url": "/static/images/butter_chicken.jpg",
        "category": "Non-Vegetarian",
        "ingredients": [
            "300g chicken (boneless)",
            "1 onion, 2 tomatoes (pureed)",
            "Butter, cream, ginger garlic paste",
            "Spices: garam masala, kasuri methi, red chili"
        ],
        "steps": [
            "Marinate chicken with yogurt and spices.",
            "Grill or cook chicken till tender.",
            "Prepare masala with butter, onions, tomato puree.",
            "Add chicken, simmer with cream and spices."
        ]
    },
    {
        "id": 7,
        "name": "Chicken Biryani",
        "image_url": "/static/images/chicken_biryani.jpg",
        "category": "Non-Vegetarian",
        "ingredients": [
            "1 cup basmati rice",
            "300g chicken",
            "Curd, biryani masala, fried onions",
            "Mint, coriander, saffron milk"
        ],
        "steps": [
            "Marinate chicken and cook partially.",
            "Layer chicken and rice, top with fried onions, mint.",
            "Add saffron milk and seal pot.",
            "Cook on dum for 20-25 mins."
        ]
    },
    {
        "id": 8,
        "name": "Egg Curry",
        "image_url": "/static/images/egg_curry.jpg",
        "category": "Non-Vegetarian",
        "ingredients": [
            "4 boiled eggs",
            "1 onion, 1 tomato, ginger garlic paste",
            "Spices: turmeric, chili, garam masala"
        ],
        "steps": [
            "Fry boiled eggs lightly.",
            "Sauté onion and tomato with spices.",
            "Add water and eggs, cook for 10 mins."
        ]
    },
    {
        "id": 9,
        "name": "Fish Fry",
        "image_url": "/static/images/fish_fry.jpg",
        "category": "Non-Vegetarian",
        "ingredients": [
            "Fish slices (200g)",
            "Lemon juice, chili powder, salt, turmeric",
            "Oil for shallow fry"
        ],
        "steps": [
            "Marinate fish with spices and lemon juice.",
            "Shallow fry until crisp and golden.",
            "Serve with onion rings and lemon wedges."
        ]
    },
    {
        "id": 10,
        "name": "Chicken 65",
        "image_url": "/static/images/chicken_65.jpg",
        "category": "Non-Vegetarian",
        "ingredients": [
            "250g boneless chicken",
            "Cornflour, curd, garlic paste",
            "Spices: chili powder, curry leaves"
        ],
        "steps": [
            "Marinate chicken in curd, spices and flour.",
            "Deep fry till golden.",
            "Toss in curry leaves and serve."
        ]
    }
]
