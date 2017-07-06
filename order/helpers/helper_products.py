from order.models import Products
import xml.etree.ElementTree as ET

class HProducts():

    """
        Get or create a Product from the db

    """
    def getOrCreateProductBySku(self, product):
        try:
            # is the product already in the db ?
            fetchedProduct = Products.objects.get(sku=product.sku)
            # return it
            return fetchedProduct
        except:
            # if not, save and return
            product.save()
            return product

    """
        Handle a product in XML format
        return a Product
    """
    def getProductFromXml(self, xmlProduct):
        # Fetching the infos
        sku         = xmlProduct.find("sku").text
        title       = xmlProduct.find("title").text
        category    = xmlProduct.find("category").text
        image_url   = xmlProduct.find("url_image").text

        # creating a new product
        product = Products.objects.create(
                        sku         = sku,
                        title       = title,
                        category    = category,
                        image_url   = image_url
                    )

        # return the product from the DB
        return self.getOrCreateProductBySku(product)


