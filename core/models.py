from django.db import models

# Create your models here.
class Product(models.Model):
    rice_name = models.CharField(max_length=100)
    hsn_code = models.CharField(max_length=20)
    gst_percent = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.rice_name
    
class Mill(models.Model):
    mill_name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    gst_number = models.CharField(max_length=20, blank=True)
    opening_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mill_name
    
class Purchase(models.Model):
    mill = models.ForeignKey(Mill, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=50)
    purchase_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bag_weight = models.IntegerField()   # 20 / 30
    bag_count = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

class Broker(models.Model):
    broker_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    gst_number = models.CharField(max_length=20, blank=True)

    opening_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.broker_name

class Sale(models.Model):
    invoice_no = models.CharField(max_length=30, unique=True, blank=True)

    customer_name = models.CharField(max_length=100)
    customer_gst = models.CharField(max_length=15, blank=True, null=True)

    broker = models.ForeignKey("Broker", on_delete=models.SET_NULL, null=True, blank=True)

    sale_date = models.DateField()

    vehicle_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    transporter_name = models.CharField(max_length=100)

    # ✅ Transport is separate
    transport_rate_per_ton = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transport_charge = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transport_paid_by_dealer = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transport_paid_by_customer = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    # ✅ Rice selling totals only (NOT include transport)
    total_quantity_kg = models.DecimalField(max_digits=10, decimal_places=2)
    taxable_amount = models.DecimalField(max_digits=12, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2)
    gst_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)  # ✅ rice_total only

    advance_received = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    balance_amount = models.DecimalField(max_digits=12, decimal_places=2)  # ✅ rice due only

    created_at = models.DateTimeField(auto_now_add=True)


# class SaleItem(models.Model):
#     sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")

#     # ✅ VERY IMPORTANT: link to purchase stock item
#     purchase_item = models.ForeignKey("PurchaseItem", on_delete=models.SET_NULL, null=True, blank=True)

#     product = models.ForeignKey("Product", on_delete=models.CASCADE)
#     mill = models.ForeignKey("Mill", on_delete=models.CASCADE)

#     bag_weight = models.IntegerField()
#     bag_count = models.IntegerField()

#     # ✅ selling (optional to store)
#     sell_rate_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     total_weight = models.DecimalField(max_digits=10, decimal_places=2)
#     sell_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

#     # ✅ buying (for internal view)
#     buy_rate_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     buy_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mill = models.ForeignKey(Mill, on_delete=models.CASCADE)

    bag_weight = models.IntegerField()
    bag_count = models.IntegerField()

    # ✅ BUY rate (from purchase stock)
    rate_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # ✅ BUY amount (bags * bag_weight * rate_per_kg)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.sale.invoice_no} - {self.mill.mill_name} - {self.product.rice_name}"


class Payment(models.Model):
    PAYMENT_TYPE = [
        ("sale", "Customer Sale Payment"),
        ("purchase", "Payment to Mill"),
    ]

    related_type = models.CharField(max_length=10, choices=PAYMENT_TYPE)
    mill = models.ForeignKey(Mill, on_delete=models.CASCADE, null=True, blank=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_mode = models.CharField(max_length=50)  # Cash, Bank, UPI
    payment_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.related_type} payment - {self.amount}"


