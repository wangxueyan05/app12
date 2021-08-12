import yaml, os


class GetData:

    def get_yml_data(self, name):
        """
        读取yaml文件数据
        :param name: 需要读取文件名字
        :return:
        """

        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
