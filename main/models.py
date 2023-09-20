from django.db import models

# Create your models here.

class Brand(models.Model):

	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to="model_img/brands/", blank=True, null=True)

	def __str__(self):
		return self.title

class Computer(models.Model):

	title = models.CharField(max_length=100, blank=False)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="model_img/computers/", blank=True, null=True)
	color = models.CharField(max_length=100, default="Black", blank=False)

	is_in_stock = models.BooleanField(default=True)
	in_stocks = models.IntegerField(default=100, blank=False)
	is_on_sale = models.BooleanField(default=True, blank=False)
	og_price = models.IntegerField(default=22000, blank=False)
	price = models.IntegerField(default=19900, blank=False)
	stars = models.FloatField(default=5.0, blank=False)
	is_recommend = models.BooleanField(default=False)

	is_laptop = models.BooleanField(default=True)
	is_gamingtype = models.BooleanField(default=False)
	has_monitor = models.BooleanField(default=True)

	CPU_BRANDS = models.TextChoices("CPU_BRANDS", "Reda Bluei")
	RAM_CHOICES = models.TextChoices("RAM_CHOICES", "4Gb 8Gb 16Gb 32Gb 64Gb")
	GPU_BRANDS = models.TextChoices("GPU_BRANDS", "Reda Bluei Greenn")
	STORAGE_CHOICES = models.TextChoices("STORAGE_CHOICES", "128Gb 256Gb 512Gb 1Tb 2Tb 4Tb")
	STORAGE_TYPE = models.TextChoices("STORAGE_TYPE", "Hdd Ssd")
	SIZE_CHOICES = models.TextChoices("SIZE_CHOICES", '14" 15.6" 16" 24" 27" 32"')
	CASE_CHOICES = models.TextChoices("CASE_CHOICES", "Mini-itx Micro-atx Atx")
	RESOLUTION_CHOICES = models.TextChoices("RESOLUTION_CHOICES", "768P 1080P 1440P 4K")
	REFRESHRATE_CHOICES = models.TextChoices("REFRESHRATE_CHOICES", "60Hz 75Hz 90Hz 120Hz 144Hz 240Hz")
	DISPLAY_CHOICES = models.TextChoices("DISPLAY_CHOICES", "Ips Tn Va Oled")
	OS_CHOICES = models.TextChoices("OS_CHOICES", "Windows11 Windows10 Non Ubuntu Archlinux")

	cpu = models.CharField(max_length=100)
	cpu_brand = models.CharField(default="Bluei", choices=CPU_BRANDS.choices, max_length=10, blank=False)
	ram = models.CharField(default="16Gb", choices=RAM_CHOICES.choices, max_length=10, blank=False)
	gpu = models.CharField(max_length=100)
	gpu_brand = models.CharField(default="Greenn", choices=GPU_BRANDS.choices, max_length=10, blank=False)
	storage = models.CharField(default="512Gb", choices=STORAGE_CHOICES.choices, max_length=10, blank=False)
	storage_type = models.CharField(default="Ssd", choices=STORAGE_TYPE.choices, max_length=10, blank=False)
	size = models.CharField(default='15.6"', choices=SIZE_CHOICES.choices, max_length=10, blank=True)
	case = models.CharField(choices=CASE_CHOICES.choices, max_length=10, blank=True)
	resolution = models.CharField(default="1080P", choices=RESOLUTION_CHOICES.choices, max_length=10, blank=True)
	refresh_rate = models.CharField(default="60Hz", choices=REFRESHRATE_CHOICES.choices, max_length=10, blank=True)
	display = models.CharField(default="Ips",choices=DISPLAY_CHOICES.choices, max_length=10, blank=True)
	weight = models.FloatField(default=1.70, blank=False)
	os = models.CharField(default="Windows11", choices=OS_CHOICES.choices, max_length=50)

	def __str__(self):
		return self.title

class Smartphone(models.Model):

	title = models.CharField(max_length=100, blank=False)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="model_img/smartphones/", blank=True, null=True)
	color = models.CharField(max_length=100, default="White", blank=False)

	is_in_stock = models.BooleanField(default=True)
	in_stocks = models.IntegerField(default=100, blank=False)
	is_on_sale = models.BooleanField(default=True, blank=False)
	og_price = models.IntegerField(default=8500, blank=False)
	price = models.IntegerField(default=7900, blank=False)
	stars = models.FloatField(default=5.0, blank=False)
	is_recommend = models.BooleanField(default=False)

	is_tablet = models.BooleanField(default=False)
	is_flagship = models.BooleanField(default=False)

	PROCESSOR_BRANDS = models.TextChoices("PROCESSOR_BRANDS", "Snapd Easy")
	RAM_CHOICES = models.TextChoices("RAM_CHOICES", "3Gb 4Gb 8Gb 6Gb 12Gb 16Gb")
	STORAGE_CHOICES = models.TextChoices("STORAGE_CHOICES", "32Gb 64Gb 128Gb 256Gb 512Gb")
	SIZE_CHOICES = models.TextChoices("SIZE_CHOICES", '5.8" 6.0" 6.2" 6.4" 6.6" 6.8" 9.7" 10.1" 12"')
	RESOLUTION_CHOICES = models.TextChoices("RESOLUTION_CHOICES", "1080P 1440P 4K")
	REFRESHRATE_CHOICES = models.TextChoices("REFRESHRATE_CHOICES", "60Hz 75Hz 90Hz 120Hz 144Hz 240Hz")
	DISPLAY_CHOICES = models.TextChoices("DISPLAY_CHOICES", "Ips Va Oled")
	OS_CHOICES = models.TextChoices("OS_CHOICES", "Android10 Android11 Android12 Android13")
	FRONTCAMERA_CHOICES = models.TextChoices("FRONTCAMERA_CHOICES", "6Mp 8Mp 10Mp 12Mp 32Mp")
	BACKCAMERA_CHOICES = models.TextChoices("BACKCAMERA_CHOICES", "10Mp 12Mp 32Mp 50Mp")
	SIM_CHOICES = models.TextChoices("SIM_CHOICES", "1Sim 2Sim")

	processor = models.CharField(max_length=100)
	processor_brand = models.CharField(default="Snapd", choices=PROCESSOR_BRANDS.choices, max_length=10, blank=False)
	ram = models.CharField(default="6Gb", choices=RAM_CHOICES.choices, max_length=10, blank=False)
	storage = models.CharField(default="128Gb", choices=STORAGE_CHOICES.choices, max_length=10, blank=False)
	size = models.CharField(default='6.2"', choices=SIZE_CHOICES.choices, max_length=10, blank=True)
	resolution = models.CharField(default="1440P", choices=RESOLUTION_CHOICES.choices, max_length=10, blank=True)
	refresh_rate = models.CharField(default="90Hz", choices=REFRESHRATE_CHOICES.choices, max_length=10, blank=True)
	display = models.CharField(default="Ips", choices=DISPLAY_CHOICES.choices, max_length=10, blank=True)
	weight = models.FloatField(default=0.14, blank=False)
	os = models.CharField(default="Android13", choices=OS_CHOICES.choices, max_length=10, blank=False)
	front_camera = models.CharField(default="10Mp", choices=FRONTCAMERA_CHOICES.choices, max_length=10, blank=False)
	back_camera = models.CharField(default="32Mp", choices=BACKCAMERA_CHOICES.choices, max_length=10, blank=False)
	sim = models.CharField(default="1Sim", choices=SIM_CHOICES.choices, max_length=10, blank=False)

	def __str__(self):
		return self.title

class Headphone(models.Model):

	title = models.CharField(max_length=100, blank=False)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="model_img/headphones/", blank=True, null=True)
	color = models.CharField(max_length=100, default="Black", blank=False)

	is_in_stock = models.BooleanField(default=True)
	in_stocks = models.IntegerField(default=100, blank=False)
	is_onsale = models.BooleanField(default=True, blank=False)
	og_price = models.IntegerField(default=1500, blank=False)
	price = models.IntegerField(default=900, blank=False)
	stars = models.FloatField(default=5.0, blank=False)
	is_recommend = models.BooleanField(default=False)

	is_bluetooth = models.BooleanField(default=True)
	is_waterproof = models.BooleanField(default=False)
	has_noise_cancelling = models.BooleanField(default=True)
	has_microphone = models.BooleanField(default=True)

	HEADPHONE_TYPES = models.TextChoices("HEADPHONE_TYPES", "Opened-back-on-ear Closed-back-on-ear Opened-back-over-ear Closed-back-over-ear In-ear")
	PORT_TYPES = models.TextChoices("PORT_TYPES", "Usb Usb-c Aux3.5")
	FREQUENCY_CHOICES = models.TextChoices("FREQUENCY_CHOICES", "20Hz-20khz 10Hz-24khz 40Hz-6800hz 4Hz-40khz")

	headphone_type = models.CharField(default="Closed-back-over-ear", choices=HEADPHONE_TYPES.choices, max_length=50, blank=False)
	port = models.CharField(default="Usb-c", choices=PORT_TYPES.choices, max_length=10, blank=False)
	frequency_response = models.CharField(default="20Hz-20khz", choices=FREQUENCY_CHOICES.choices, max_length=50, blank=False)

	def __str__(self):
		return self.title

class Cloth(models.Model):

	title = models.CharField(max_length=100, blank=False)
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="model_img/cloths/", blank=True, null=True)
	color = models.CharField(max_length=100, default="White", blank=False)

	is_in_stock = models.BooleanField(default=True)
	in_stocks = models.IntegerField(default=100, blank=False)
	is_onsale = models.BooleanField(default=True, blank=False)
	og_price = models.IntegerField(default=1500, blank=False)
	price = models.IntegerField(default=900, blank=False)
	stars = models.FloatField(default=5.0, blank=False)
	is_recommend = models.BooleanField(default=False)

	GENDER_CHOICES = models.TextChoices("GENDER_CHOICES", "Male Female Unisex")
	CLOTH_TYPES = models.TextChoices("CLOTH_TYPES", "T-shirt Sleeveless-shirt Sweatshirt Hoody Dress-shirt ")
	SIZE_CHOICES = models.TextChoices("SIZE_CHOICES", "S M L XL XXL")

	gender = models.CharField(default="Unisex", choices=GENDER_CHOICES.choices, max_length=10, blank=False)
	cloth_type = models.CharField(default="T-shirt", choices=CLOTH_TYPES.choices, max_length=50, blank=False)
	size = models.CharField(default="S", choices=SIZE_CHOICES.choices, max_length=5, blank=False)

	def __str__(self):
		return self.title