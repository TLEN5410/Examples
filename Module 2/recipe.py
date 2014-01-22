def bake_pizza():
	""" This function bakes a pizza """
	duration = 60
	temp = 300
	
def bake_chicken():
	""" This function bakes a chicken """
	duration = 45
	temp = 400
	
def main():
	# Returns a fresh new Pizza
	pizza = prepare_dough() 
	# Returns the Pizza passed in, but with sauce added on ot.
	pizza = add_sauce(pizza, "tomato")
	# Returns the same Pizza passed in, but with toppings added on it.
	pizza = add_topings(pizza, "pepperoni", "green olives")
	# Returns a fully baked pizza
	pizza = bake_pizza(pizza)
	
	# Returns a new, trimmed chicken
	chicken = trim_chicken()
	# Returns the same chicken passed in, but with some seasoning added
	chicken = add_seasoning(chicken, "pepper", "salt")
	# Returns a fully baked chicken
	chicken = bake_chicken(chicken)
	
main()
	