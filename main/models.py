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

	is_instock = models.BooleanField(default=True)
	instocks = models.IntegerField(default=100, blank=False)
	is_onsale = models.BooleanField(default=True)
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
	storage = models.CharField(max_length=10)
	storage_type = models.CharField(default="Ssd", choices=STORAGE_TYPE.choices, max_length=10, blank=False)
	size = models.CharField(default='15.6"', choices=SIZE_CHOICES.choices, max_length=10, blank=True)
	case = models.CharField(choices=CASE_CHOICES.choices, max_length=10, blank=True)
	resolution = models.CharField(default="1080P", choices=RESOLUTION_CHOICES.choices, max_length=10, blank=True)
	refreshrate = models.CharField(default="60Hz", choices=REFRESHRATE_CHOICES.choices, max_length=10, blank=True)
	display = models.CharField(default="Ips",choices=DISPLAY_CHOICES.choices, max_length=10, blank=True)
	weight = models.FloatField(default=1.70, blank=False)
	os = models.CharField(default="Windows11", choices=OS_CHOICES.choices, max_length=50)

	def __str__(self):
		return self.title