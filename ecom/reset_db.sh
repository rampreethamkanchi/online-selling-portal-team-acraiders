#!/bin/bash

# Remove default database
rm db.sqlite3

# Remove migrations
rm -rf store/migrations

# Create new migrations
# python manage.py makemigrations ecom
python manage.py makemigrations store

# Apply migrations
python manage.py migrate

# Create superuser
# python manage.py createsuperuser 
echo "from django.contrib.auth.models import User; User.objects.create_superuser('acraiders', 'acraiders@gmail.com', 'acr@2004')" | python manage.py shell
# echo "from django.contrib.auth.models import User; User.objects.create(username='rampreetham', email='rampreethamkanchi@gmail.com', password='ramu@2004')" | python manage.py shell
# create a customer for the superuser , with city and phone
echo "from django.contrib.auth.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='acraiders'), city='Nellore', phone='9032232817')" | python manage.py shell
# echo "from django.contrib.auth.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='rampreetham'), city='Nellore', phone='9032256780')" | python manage.py shell
# echo "from store.models import Customer; Customer.objects.create(user=User.objects.get(username='acraiders'), )" | python manage.py shell
#add these categories
echo "from store.models import Category; Category.objects.create(name='Electronics and Technology', description='Explore a wide range of cutting-edge electronics and technology products on our platform. From smartphones to laptops, cameras to gaming consoles, and everything in between, find the latest gadgets and devices to suit your needs. Whether you\'re a tech enthusiast, a professional, or just looking to upgrade your devices, browse through our extensive collection of electronics and technology products from top brands.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Books', description='Immerse yourself in the world of literature with our diverse selection of books. From best-selling novels to academic textbooks, fiction to non-fiction, we have something for every reader. Discover timeless classics, explore new releases, or find rare and collectible editions. Whether you\'re passionate about fiction, history, science, or any other genre, you\'ll find a treasure trove of books waiting to be explored on our platform.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Real Estate', description='Find your dream property with ease on our real estate platform. Whether you\'re looking to buy, sell, or rent, we connect you with a wide range of residential and commercial properties. From cozy apartments to spacious villas, modern office spaces to retail storefronts, explore listings from trusted sellers and real estate agents. With detailed property descriptions, photos, and location maps, finding the perfect property has never been easier.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Cars and Bikes', description='Hit the road in style with our collection of cars and bikes. Whether you\'re in the market for a sleek sedan, a rugged SUV, a powerful sports car, or a reliable commuter bike, we\'ve got you covered. Browse through listings from private sellers and dealerships to find the perfect vehicle to suit your preferences and budget. With detailed specifications, photos, and seller contact information, buying or selling a car or bike is hassle-free.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Education and Learning', description='Invest in your future with our range of education and learning resources. Whether you\'re a student, a professional looking to upskill, or someone interested in personal development, discover courses, tutorials, and educational materials across various subjects and disciplines. From online courses to tutoring services, exam preparation materials to language learning resources, embark on a journey of lifelong learning and growth with our platform.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Home and Lifestyle', description='Transform your living space and enhance your lifestyle with our home and lifestyle products. From furniture to decor, appliances to kitchenware, and wellness products to fashion accessories, find everything you need to create a stylish and comfortable home. Explore curated collections, shop for unique and artisanal items, and discover inspiration for your home and personal style. With quality products from trusted sellers, elevate your living experience with our platform.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Cellphone', description='Stay connected and stay ahead with the latest cellphones and accessories. Whether you\'re in need of a flagship smartphone, a budget-friendly device, or accessories like cases, chargers, and headphones, find everything you need to stay connected on the go. Browse through a wide selection of brands and models, compare specifications and prices, and make informed decisions about your next cellphone purchase. With hassle-free shopping and secure transactions, upgrading your mobile experience has never been easier.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Fashion and Apparel', description='Elevate your style with our fashion and apparel collection. Explore the latest trends in clothing, footwear, accessories, and more for men, women, and children. From casual wear to formal attire, streetwear to haute couture, find curated collections from top fashion brands and designers. Whether you\'re looking for everyday essentials or statement pieces for special occasions, shop with confidence and express your unique sense of style with our diverse range of fashion products.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Sports and Outdoors', description='Gear up for adventure with our sports and outdoors category. Whether you\'re an avid athlete, a weekend warrior, or someone who loves the great outdoors, discover equipment, apparel, and accessories for all your favorite activities. From team sports like football and basketball to individual pursuits like hiking, camping, and cycling, find everything you need to stay active and enjoy your favorite pastimes. With high-quality gear from trusted brands, explore new horizons and embrace the spirit of adventure with our sports and outdoors products.')" | python manage.py shell
echo "from store.models import Category; Category.objects.create(name='Miscellaneous and Others', description='Discover a diverse assortment of unique finds and unexpected treasures in our Miscellaneous and Others section. From quirky collectibles to rare antiques, handmade crafts to DIY supplies, explore a world of eclectic wonders that defy categorization. Whether you\'re seeking a one-of-a-kind gift or simply indulging your curiosity, this is the place to find the extraordinary amidst the ordinary. Dive in and uncover the unexpected!')" | python manage.py shell