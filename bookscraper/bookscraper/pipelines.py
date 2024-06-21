# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        value = adapter.get("price") #for converting price from £ to $
        adapter["price"] =  value.replace("£","$")
        
        value = adapter.get("price_excl_tax") #for converting price from £ to $
        adapter["price_excl_tax"] =  value.replace("£","$")
        
        value = adapter.get("price_incl_tax") #for converting price from £ to $
        adapter["price_incl_tax"] =  value.replace("£","$")
        
        value = adapter.get("tax") #for converting tax from £ to $
        adapter["tax"] =  value.replace("£","$")
        
        
        value = adapter.get("star")
        new_value = value.split(" ")
        if new_value[1] == "Zero":
            adapter["star"] = 0
            
        elif new_value[1] == "One":
            adapter["star"] = 1
        elif new_value[1] == "Two":
            adapter["star"] = 2
        
        elif new_value[1] == "Three":
            adapter["star"] = 3
            
        elif new_value[1] == "Four":
            adapter["star"] = 4
        elif new_value[1] == "Five":
            adapter["star"] = 5
            
            
        return item
