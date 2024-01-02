from itemadapter import ItemAdapter

class MysqlDemoPipeline:
    def process_item(self, item, spider):
        return item