from pyexpat import model
from tabnanny import verbose
from unicodedata import category
from django.db import models
from simple_history.models import HistoricalRecords
from base.models import BaseModel

#el modelo hereda del modelo Base en la app base 
class MeasureUnit(BaseModel):

    description = models.CharField(max_length=50, blank=False,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField("Descripcion",max_length=50,unique=True,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descount_value = models.PositiveIntegerField(default=0) 
    category_product =models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Indicador de oferta")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicador de oferta"
        verbose_name_plural = "Indicadores de ofertas"

    def __str__(self):
        return f'Oferta de la categoria{self.category_product} : {self.descount_value}%' 

class Product(BaseModel):
   
    name = models.CharField("Nombre de producto", max_length=150,unique=True,blank=False,null=False)
    descripcion = models.TextField("Descripcion de producto",blank = False, null = False)
    measuere_unit = models.ForeignKey(MeasureUnit,on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    category_product = models.ForeignKey(CategoryProduct,on_delete=models.CASCADE, verbose_name="Categoria de producto", null=True)
    image = models.ImageField("Imagen del producto", upload_to="products/",blank=True,null=True)
    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
