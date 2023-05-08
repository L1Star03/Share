from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd

class Spider():

    def __init__(self) -> None:
        driver = self.driver = webdriver.Edge('msedgedriver.exe')
        # Edge.option.add_argument('headless')
        driver.implicitly_wait(10)  # 自适应等待
        # self.url = 'https://item.jd.com/100051233989.html#comment'
        # self.url = 'https://item.jd.com/100022202065.html#comment'
        self.url_ls = [i[0]+'#comment' if '#comment' not in i[0] else i[0] for i in pd.read_excel('./urls/urls.xlsx', header=None).values]

    def find_x(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath)
        # WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH, xpath))
        except:
            return False

    def main(self, url):
        self.driver.get(url)
        driver = self.driver
        name = self.find_x('/html/body/div[6]/div/div[2]/div[1]').get_attribute('textContent').strip().replace('*', 'x').replace('/', '')
        # 文件名里面不能有"*"所以这里要进行替换
        cost = "".join(self.driver.find_element(By.CLASS_NAME, 'p-price').get_attribute('textContent').strip().split())
        print(name)
        print(cost)
        page = 1
        with open('./cost/cost.txt', 'a+') as file:
            if 'name' not in file.read():
                file.writelines(f'{name} : {cost}\n')
        with open(f'./comments/{name}.txt', 'w+') as file:
            for j in range(100):
                print(f'当前page{page}')
                page += 1
                if self.find_x('/html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]').get_attribute('textContent') == '「暂无评价」':
                    file.writelines('end')
                    break
                for i in range(1, 11):
                    try:
                        file.writelines(self.find_x(f'/html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div[2]/p').get_attribute('textContent'))
                        # file.writelines(' ')
                        # file.writelines(self.find('/html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[{i}]/div[2]/div[4]/div[1]/span[4]').get_attribute('textContent'))
                        file.write('\n')
                    except AttributeError:
                        break
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    next = self.driver.find_element(By.CLASS_NAME, 'ui-pager-next')
                    if next.get_attribute('textContent') == '下一页':
                        driver.execute_script("$(arguments[0]).click()", next)
                except:
                    print('没有找到下一页')
                    break
                time.sleep(0.8 + random.random())
        # 暂无评价 /html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]

    def enumerate_urls(self):
        for url in self.url_ls:
            self.main(url)

class WordCloud():
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    s = Spider()
    s.enumerate_urls()