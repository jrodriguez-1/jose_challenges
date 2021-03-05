
import clothes 

class Wardrobe:
    
    def __intit__(self):
        self.my_clothing = []
        self.my_clothing_count = 0
        self.clothing = Clothes.objects()


    def add_item(self,color,style):
        self.my_clothing_count += 1
        self.my_clothing.append(self.clothing)
        if style in self.clothing == 'shorts' or 'shoes' or 'pants':
            print(f'{self.color} {self.style} has been added.')
        else:
            print(f'A {self.color} {self.style} has been added.')

    def remove_item(self,color,style):
        self.my_clothing_count -= 1
        for item in self.my_clothing:
            if item == style and color:
                self.my_clothing.remove(self.clothing[item])

            if style in self.clothing == 'shorts' or 'shoes' or 'pants':
                print(f'{self.color} {self.style} has been removed.')
            else:
                print(f'A {self.color} {self.style} has been removed.')

    def remove_all(self):
        self.my_clothing_count = 0
        for items in self.my_clothing:
            self.my_clothing.clear(items)
        print('All clothing has been removed.')

    def remove_by_color(self,color):
        self.my_clothing_count -= 1
        for item in self.my_clothing:
            if item == color:
                self.my_clothing.remove(self.clothing[item])

    def remove_by_style(self,style):
        self.my_clothing_count -= 1
        for item in self.my_clothing:
            if item == style:
                self.my_clothing.remove(self.clothing[item])
            
    def remove_all_style(self,style):
        for items in self.my_clothing:
            if items == style:
                self.my_clothing.remove(items)

            self.my_clothing_count -= len(items)
    
    def remove_all_color(self,color):
        for items in self.my_clothing:
            if items == color:
                self.my_clothing.remove(items)

            self.my_clothing_count -= len(items)

    def max_capacity(self):
        if self.my_clothing_count == 10:
            print('Maximum limit has been reached. No more clothes')


wardrobe1 = Wardrobe()

print(wardrobe1.add_item('green','shirt'))

print(wardrobe.remove_item('green','shirt'))

print(wardrobe.remove_all())

print(wardrobe.remove_by_color('green'))

print(wardrobe.remove_by_style('shirt'))

print(wardrobe.remove_all_style('shirt'))

print(wardrobe.remove_all_color('green'))




