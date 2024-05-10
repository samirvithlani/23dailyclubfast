#add product
#view products
#delete product
#update product

#add to cart
#checkout

from functools import reduce

class Amazone:
    
    def __init__(self):
        self.products = []
        self.cart = []
        
    def addProduct(self):
        #pid pname price qty color
        pid = int(input("Enter product id: "))
        pname = input("Enter product name: ")
        pprice = float(input("Enter product price: "))
        pqty = int(input("Enter product qty: "))
        product= {"pid":pid, "pname":pname, "pprice":pprice, "pqty":pqty}
        print("Product added successfully")
        self.products.append(product)
        
        
    def viewProduct(self):
        print("Product id\tProduct Name\tProduct Price\tProduct Qty")
        print("---------------------------------------------------------")
        for product in self.products:
            print(f"{product['pid']}\t\t{product['pname']}\t\t{product['pprice']}\t\t{product['pqty']}")
    def deleteProduct(self,pid):
        self.products = [product for product in self.products if product['pid']!=pid]
        print("Product deleted successfully")
        self.viewProduct()
        
    def updateProduct(self,pid):
        
        pname = input("Enter product name to update: ")
        pprice = float(input("Enter product price to update: "))
        pqty = int(input("Enter product qty to update: "))
        ##first find product from dict
        for product in self.products:
            if product['pid']==pid:
                product['pname'] = pname
                product['pprice'] = pprice
                product['pqty'] = pqty
                break
        
        print("Product updated successfully")    
        
    def addToCart(self,pid):
        #//find product with id
        for product in self.products:
            if product['pid']==pid:
                self.cart.append(product)
                break
        
        print("Product added to cart successfully")    
        
        
  
    def checkout(self):
        print("Product id\tProduct Name\tProduct Price\tProduct Qty")
        print("---------------------------------------------------------")
        for product in self.products:
            print(f"{product['pid']}\t\t{product['pname']}\t\t{product['pprice']}\t\t{product['pqty']}")

        total_cart_price = reduce(lambda total, product: total + (product['pprice'] * product['pqty']), self.cart, 0)

        print(f"Total amount to pay: {total_cart_price}")
        cchoice = input("Do you want to checkout? y/n")
        if cchoice=='y':
            print("Thank you for shopping with us")
            self.cart = []
        else:
            print("Continue shopping")    
            

        
        


#match case...

a = Amazone()
while True:
    
    print("1. Add Product")
    print("2. View Product")
    print("3. Delete Product")
    print("4. Update Product")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            a.addProduct()
        case 2:
            a.viewProduct()
        case 3:
            print("enter id to delete product")
            id = int(input())
            a.deleteProduct(id)
        case 4:
            print("enter id to update product")
            id = int(input())
            a.updateProduct(id)
        case 5:
            print("enter id to add product to cart")
            id = int(input())
            a.addToCart(id)            
        case 6:
            a.checkout()    
        case _:
            break    
                
                
            
        
    
    
    
                
    
        
