from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = (
            'title',
            'code'
        )


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = (
            'title',
        )


class WarehouseSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField(source='material.title')

    class Meta:
        model = models.Warehouse
        fields = (
            'material',
            'remainder',
            'price',
        )


class RequestSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()


class ProductMaterialSerializer(serializers.ModelSerializer):
    material = serializers.StringRelatedField(source='material.title')

    class Meta:
        model = models.ProductMaterial
        fields = (
            'material',
        )


class ProductResultSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    product_materials = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = (
            'title',
            'quantity',
            'product_materials'
        )

    def get_product_materials(self, obj):
        result = []
        quantity = obj.quantity  # 30 ta ko'ylak
        materials = obj.materials.all().prefetch_related('material__warehouses')
        for material in materials:
            warehouses = material.material.warehouses.all()

            title = material.material.title

            limit = round((int(quantity) * material.quantity), 4)
            print(limit)

            for warehouse in warehouses:

                price = warehouse.price
                if limit > warehouse.remainder:
                    qty = warehouse.remainder
                    limit = limit - qty
                else:
                    qty = limit

                result.append({
                    'warehouse_id': warehouse.id,
                    'material_name': title,
                    'qty': qty,
                    'price': price,
                })

        return result


class ProductResultSerializer2(serializers.ModelSerializer):
    quantity = serializers.IntegerField()

    class Meta:
        model = models.Product
        fields = (
            'title',
            'quantity',
        )
