#!/bin/bash

# Remove default database
rm db.sqlite3

# Remove migrations
rm -rf store/migrations

# Create new migrations
# python3 manage.py makemigrations ecom
python3 manage.py makemigrations store

# Apply migrations
python3 manage.py migrate

# Create superuser
# python3 manage.py createsuperuser 
# echo "from store.models import User; User.objects.create_superuser('acraiders', 'acraiders@gmail.com', 'acr@2004')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='rampreetham', email='rampreethamkanchi@gmail.com', password='ramu@2004')" | python3 manage.py shell
# creating users
echo "from store.models import User; User.objects.create_superuser(username='acraiders', email='acraiders@gmail.com', password='xyz@2004', first_name='acraiders', last_name='owner')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='rampreetham', email='rampreethamkanchi@gmail.com', password='xyz@2004', first_name='Ram Preetham', last_name='Kanchi')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='jaswanth', email='jaswanth@gmail.com', password='xyz@2004', first_name='Jaswanth', last_name='Mantri')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='varun', email='varun@gmail.com', password='xyz@2004', first_name='Varun', last_name='Mupparaju')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='nishnath', email='nishnath@gmail.com', password='xyz@2004', first_name='Nishnath', last_name='Parimi')" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='karthikeya', email='karthikeya@gmail.com', password='xyz@2004', first_name='Karthikeya', last_name='Poondla')" | python3 manage.py shell
echo "from store.models import User; user = User.objects.create(username='karthikeya', email='karthikeya@gmail.com', first_name='Karthikeya', last_name='Poondla'); user.set_password('xyz@2004'); user.save()" | python3 manage.py shell
echo "from store.models import User; user = User.objects.create(username='rampreetham',email = 'rampreetham@gmail.com', first_name='Rampreetham', last_name='Kanchi'); user.set_password('xyz@2004'); user.save()" | python3 manage.py shell
echo "from store.models import User; user = User.objects.create(username='jaswanth',email = 'mantrijaswanth@gmail.com', first_name='Jaswanth', last_name='Mantri'); user.set_password('xyz@2004'); user.save()" | python3 manage.py shell
echo "from store.models import User; user = User.objects.create(username='varun',email = 'varun.mupparaju007@gmail.com', first_name='Varun', last_name='Mupparaju'); user.set_password('xyz@2004'); user.save()" | python3 manage.py shell
echo "from store.models import User; user = User.objects.create(username='nishnath',email = 'nishnath@gmail.com', first_name='Nishnath', last_name='Parimi'); user.set_password('xyz@2004'); user.save()" | python3 manage.py shell
# echo "from store.models import User; User.objects.create(username='vamshi', email='rampreethamkanchi@gmail.com', password='ramu@2004', first_name='Vamshi', last_name='Krishna')" | python3 manage.py shell
# create a customer for the superuser , with city and phone
# echo "from store.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='acraiders'), phone='9032232817')" | python3 manage.py shell
# echo "from store.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='rampreetham'), phone='9032256780')" | python3 manage.py shell
#creating some customers from users
echo "from store.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='jaswanth'), phone='9032256780')" | python3 manage.py shell
echo "from store.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='varun'), phone='9032256781')" | python3 manage.py shell
echo "from store.models import User; from store.models import Customer; Customer.objects.create(user=User.objects.get(username='nishnath'), phone='9032256782')" | python3 manage.py shell
# add address to the customers
# class Address(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     city = models.CharField(max_length=20, choices=cities)
#     state = models.CharField(max_length=50, choices=STATE_CHOICES)
#     pincode = models.CharField(
#         max_length=6,
#         validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')],
#     )
#     street = models.CharField(max_length=50)
#     house_no = models.CharField(max_length=50, null=True, blank=True)
# jaswanth , varun , nishnath are the customers
echo "from store.models import User; from store.models import Customer; from store.models import Address; Address.objects.create(customer=Customer.objects.get(user=User.objects.get(username='jaswanth')), city='Nellore', state='Andhra Pradesh', pincode='500072', street='Kanchi Nagar', house_no='12/543/1')" | python3 manage.py shell
echo "from store.models import User; from store.models import Customer; from store.models import Address; Address.objects.create(customer=Customer.objects.get(user=User.objects.get(username='varun')), city='Hyderabad', state='Telegana', pincode='500073', street='Mupparaju Nagar', house_no='12/543/2')" | python3 manage.py shell
echo "from store.models import User; from store.models import Customer; from store.models import Address; Address.objects.create(customer=Customer.objects.get(user=User.objects.get(username='nishnath')), city='Nellore', state='Andhra Pradesh', pincode='500072', street='Parimi Nagar', house_no='12/543/3')" | python3 manage.py shell
#     def __str__(self):
#         return self.city
#     class Meta:
#         verbose_name_plural = 'addresses'
#
# echo "from store.models import Customer; Customer.objects.create(user=User.objects.get(username='acraiders'), )" | python3 manage.py shell
#add these categories
#creating managers for rampreetham and karthikeya
# this is manger model
# class Manager(models.Model):
#     gender_choices = [
#         ('male','male'),
#         ('female','female'),
#         ('others','others'),
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=20, choices=cities)
#     phone = PhoneNumberField(unique=True)
#     state = models.CharField(max_length=50, choices=STATE_CHOICES)
#     pincode = models.CharField(
#         max_length=6,
#         validators=[RegexValidator('^[0-9]{6}$', 'Invalid postal code')],
#     )
#     street = models.CharField(max_length=50)
#     house_no = models.CharField(max_length=50, null=True, blank=True)
#     dob = models.DateField()
#     gender = models.CharField(max_length=50, choices=gender_choices)
#     locality = models.CharField(max_length=50)
#     #add to Managers group
#     # user.groups.add(Group.objects.get(name='Managers'))
#     def __str__(self):
#         return str(self.user)
#     class Meta:
#         verbose_name_plural = 'managers'
#     def save(self, *args, **kwargs):
#         # Call the parent class's save method
#         super().save(*args, **kwargs)
#         self.user.is_superuser = True
#         self.user.is_staff = True
#         self.user.save(update_fields=['is_superuser', 'is_staff'])

echo "from store.models import User; from store.models import Manager; Manager.objects.create(user=User.objects.get(username='rampreetham'),gender='male',phone='9032256785',city='Nellore', state='Andhra Pradesh', pincode='500072', street='Kanchi Nagar', dob='2004-04-20', locality='Kanchi Nagar')" | python3 manage.py shell
echo "from store.models import User; from store.models import Manager; Manager.objects.create(user=User.objects.get(username='karthikeya'), gender='male',phone='9032256786',city='Hyderabad', state='Telangana', pincode='500073', street='Poondla Nagar', dob='2004-04-21', locality='Poondla Nagar', house_no='12/543/1')" | python3 manage.py shell 

echo "from store.models import Category; Category.objects.create(name='Electronics and Technology', description='Explore a wide range of cutting-edge electronics and technology products on our platform. From smartphones to laptops, cameras to gaming consoles, and everything in between, find the latest gadgets and devices to suit your needs. Whether you\'re a tech enthusiast, a professional, or just looking to upgrade your devices, browse through our extensive collection of electronics and technology products from top brands.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Books', description='Immerse yourself in the world of literature with our diverse selection of books. From best-selling novels to academic textbooks, fiction to non-fiction, we have something for every reader. Discover timeless classics, explore new releases, or find rare and collectible editions. Whether you\'re passionate about fiction, history, science, or any other genre, you\'ll find a treasure trove of books waiting to be explored on our platform.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Real Estate', description='Find your dream property with ease on our real estate platform. Whether you\'re looking to buy, sell, or rent, we connect you with a wide range of residential and commercial properties. From cozy apartments to spacious villas, modern office spaces to retail storefronts, explore listings from trusted sellers and real estate agents. With detailed property descriptions, photos, and location maps, finding the perfect property has never been easier.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Cars and Bikes', description='Hit the road in style with our collection of cars and bikes. Whether you\'re in the market for a sleek sedan, a rugged SUV, a powerful sports car, or a reliable commuter bike, we\'ve got you covered. Browse through listings from private sellers and dealerships to find the perfect vehicle to suit your preferences and budget. With detailed specifications, photos, and seller contact information, buying or selling a car or bike is hassle-free.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Education and Learning', description='Invest in your future with our range of education and learning resources. Whether you\'re a student, a professional looking to upskill, or someone interested in personal development, discover courses, tutorials, and educational materials across various subjects and disciplines. From online courses to tutoring services, exam preparation materials to language learning resources, embark on a journey of lifelong learning and growth with our platform.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Home and Lifestyle', description='Transform your living space and enhance your lifestyle with our home and lifestyle products. From furniture to decor, appliances to kitchenware, and wellness products to fashion accessories, find everything you need to create a stylish and comfortable home. Explore curated collections, shop for unique and artisanal items, and discover inspiration for your home and personal style. With quality products from trusted sellers, elevate your living experience with our platform.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Cellphone', description='Stay connected and stay ahead with the latest cellphones and accessories. Whether you\'re in need of a flagship smartphone, a budget-friendly device, or accessories like cases, chargers, and headphones, find everything you need to stay connected on the go. Browse through a wide selection of brands and models, compare specifications and prices, and make informed decisions about your next cellphone purchase. With hassle-free shopping and secure transactions, upgrading your mobile experience has never been easier.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Fashion and Apparel', description='Elevate your style with our fashion and apparel collection. Explore the latest trends in clothing, footwear, accessories, and more for men, women, and children. From casual wear to formal attire, streetwear to haute couture, find curated collections from top fashion brands and designers. Whether you\'re looking for everyday essentials or statement pieces for special occasions, shop with confidence and express your unique sense of style with our diverse range of fashion products.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Sports and Outdoors', description='Gear up for adventure with our sports and outdoors category. Whether you\'re an avid athlete, a weekend warrior, or someone who loves the great outdoors, discover equipment, apparel, and accessories for all your favorite activities. From team sports like football and basketball to individual pursuits like hiking, camping, and cycling, find everything you need to stay active and enjoy your favorite pastimes. With high-quality gear from trusted brands, explore new horizons and embrace the spirit of adventure with our sports and outdoors products.')" | python3 manage.py shell
echo "from store.models import Category; Category.objects.create(name='Miscellaneous and Others', description='Discover a diverse assortment of unique finds and unexpected treasures in our Miscellaneous and Others section. From quirky collectibles to rare antiques, handmade crafts to DIY supplies, explore a world of eclectic wonders that defy categorization. Whether you\'re seeking a one-of-a-kind gift or simply indulging your curiosity, this is the place to find the extraordinary amidst the ordinary. Dive in and uncover the unexpected!')" | python3 manage.py shell

#creating products
# class Product(models.Model): 
#     id = models.AutoField(primary_key=True)
#     p_name = models.CharField("Product name",max_length=100)
#     m_name = models.CharField("Name of the manufacturing company",max_length=100, default='unknown', blank=True)
#     is_light = models.BooleanField("Can you ship to other city?",default=False)
#     seller = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     sale_price = models.PositiveBigIntegerField(default=0)
#     # price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
#     price = models.PositiveBigIntegerField(default=0)
#     #set default category to others
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=get_default_category)
#     description = models.TextField()
#     #upload upto 5 images to f"products/{id}/" folder
#     image1 = models.ImageField(upload_to="products/")
#     image2 = models.ImageField(upload_to="products/",blank=True, null=True)
#     image3 = models.ImageField(upload_to="products/",blank=True, null=True)
#     image4 = models.ImageField(upload_to="products/",blank=True, null=True)
#     image5 = models.ImageField(upload_to="products/",blank=True, null=True)
#     city = models.CharField(max_length=20, choices=cities)
#     age = models.DurationField("Age of product",default=datetime.timedelta(0),blank=True)
#     # quantity = models.IntegerField(default=1,blank=True)
#     quantity = models.PositiveBigIntegerField(default=1,blank=True)
#     # age = models.TimeField(default=datetime.time(0, 0))
#     # slug = models.SlugField(unique=True, max_length=100,)

#     # Add sales stuff
#     is_sale = models.BooleanField(default=True)
#     # sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


#     def __str__(self):
#         return self.p_name
# jaswanth , varun , nishnath are the sellers
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='Samsung Galaxy S21 Ultra', m_name='Samsung', is_light=True, seller=Customer.objects.get(user=User.objects.get(username='varun')), sale_price=105000, price=110000, category=Category.objects.get(name='Electronics and Technology'), description='Samsung Galaxy S21 Ultra 5G smartphone runs on Android v11 operating system. The phone is powered by Octa core (2.9 GHz, Single core, Cortex X1 + 2.8 GHz, Tri core, Cortex A78 + 2.2 GHz, Quad core, Cortex A55) processor. It runs on the Samsung Exynos 2100 Chipset. It has 12 GB RAM and 256 GB internal storage.', image1='products/samsung-galaxy-s21-ultra.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
# give random number of images in following products, max 5
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='Apple iPhone 12 Pro Max', m_name='Apple', is_light=True, seller=Customer.objects.get(user=User.objects.get(username='jaswanth')), sale_price=125000, price=130000, category=Category.objects.get(name='Electronics and Technology'), description='Apple iPhone 12 Pro Max smartphone runs on iOS v14.1 operating system. The phone is powered by Hexa Core (2.65 GHz, Dual core, Lightning + 1.8 GHz, Quad core, Thunder) processor. It runs on the Apple A14 Bionic Chipset. It has 6 GB RAM and 128 GB internal storage.', image1='products/apple-iphone-12-pro-max.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='OnePlus 9 Pro', m_name='OnePlus', is_light=False, seller=Customer.objects.get(user=User.objects.get(username='nishnath')), sale_price=65000, price=70000, category=Category.objects.get(name='Electronics and Technology'), description='OnePlus 9 Pro smartphone runs on Android v11 operating system. The phone is powered by Octa core (2.84 GHz, Single core, Kryo 680 + 2.42 GHz, Tri core, Kryo 680 + 1.8 GHz, Quad core, Kryo 680) processor. It runs on the Qualcomm Snapdragon 888 Chipset. It has 8 GB RAM and 128 GB internal storage.', image1='products/oneplus-9-pro.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
#give image1, image2, image3
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='Dell XPS 15', m_name='Dell', is_light=False, seller=Customer.objects.get(user=User.objects.get(username='varun')), sale_price=150000, price=160000, category=Category.objects.get(name='Electronics and Technology'), description='Dell XPS 15 laptop has a 15.6-inch display. It is powered by a Core i7 processor and it comes with 16GB of RAM. The Dell XPS 15 packs 512GB of SSD storage.', image1='products/dell-xps-15.jpg', image2='products/dell-xps-15-2.jpg', image3='products/dell-xps-15-3.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
#other category
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='The Alchemist', m_name='Paulo Coelho', is_light=True, seller=Customer.objects.get(user=User.objects.get(username='jaswanth')), sale_price=300, price=350, category=Category.objects.get(name='Books'), description='The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it has been translated into numerous languages and has sold over 65 million copies worldwide. The story follows a young Andalusian shepherd named Santiago who dreams of finding a hidden treasure in Egypt. Along the way, he encounters various characters and experiences that teach him valuable lessons about life, love, and destiny.', image1='products/the-alchemist.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
# is light is true
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='The Great Gatsby', m_name='F. Scott Fitzgerald', is_light=True, seller=Customer.objects.get(user=User.objects.get(username='varun')), sale_price=200, price=250, category=Category.objects.get(name='Books'), description='The Great Gatsby is a novel by American author F. Scott Fitzgerald that was first published in 1925. Set in the Jazz Age on Long Island, the story follows the young and mysterious millionaire Jay Gatsby and his obsession with the beautiful Daisy Buchanan. The novel explores themes of wealth, love, and the American Dream, and is considered a classic of American literature.', image1='products/the-great-gatsby.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
#other category with imaage 1, image 2, image 3, image 4
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='The Lord of the Rings', m_name='J.R.R. Tolkien', is_light=True, seller=Customer.objects.get(user=User.objects.get(username='nishnath')), sale_price=500, price=600, category=Category.objects.get(name='Books'), description='The Lord of the Rings is an epic fantasy novel by British author J.R.R. Tolkien that was first published in three volumes between 1954 and 1955. Set in the fictional world of Middle-earth, the story follows the quest of the hobbit Frodo Baggins to destroy the One Ring and defeat the Dark Lord Sauron. Along the way, he is joined by a fellowship of diverse characters who aid him in his journey. The novel explores themes of heroism, friendship, and the struggle between good and evil.', image1='products/the-lord-of-the-rings.jpg', image2='products/the-lord-of-the-rings-2.jpg', image3='products/the-lord-of-the-rings-3.jpg', image4='products/the-lord-of-the-rings-4.jpg', city='Nellore', age=timedelta(days=0), quantity=10)" | python3 manage.py shell
#other category real estate
echo "from store.models import User; from store.models import Product; from store.models import Category; from store.models import Customer; from datetime import timedelta; Product.objects.create(p_name='Luxury Villa in Goa', m_name='Goa Realty', is_light=False, seller=Customer.objects.get(user=User.objects.get(username='jaswanth')), sale_price=50000000, price=55000000, category=Category.objects.get(name='Real Estate'), description='This luxurious villa is located in the heart of Goa and offers stunning views of the Arabian Sea. Spread across 2 acres of lush greenery, the property features 5 spacious bedrooms, a private pool, and a landscaped garden. With modern amenities and elegant interiors, this villa is the perfect retreat for those seeking a peaceful and luxurious lifestyle.', image1='products/luxury-villa-goa.jpg', city='Goa', age=timedelta(days=0), quantity=1)" | python3 manage.py shell
