import ecommerce.shipping       #imports whole module from package
ecommerce.shipping.calc_shipping()


from ecommerce.shipping import calc_shipping        #imports specific method from module and package
calc_shipping()