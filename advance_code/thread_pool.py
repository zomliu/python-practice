from concurrent.futures import ThreadPoolExecutor
import time

def down_images(url):
    print('begin：', url)
    time.sleep(1)
    print('finished')

    return f'Done: {url}'

if __name__ == '__main__':
    urls = [
        'url1', 'url2', 'url3', 'url4', 'url5'
    ]
    with ThreadPoolExecutor(max_workers=3) as executor:    # 不用 with 的话，需要手动关闭线程池: executor.shutdown()
        # approach 1
        # for url in urls:
        #     executor.submit(down_images, url)

        # approach 2
        # future_list = [executor.submit(down_images, url) for url in urls]
        # for future in future_list:
        #     print(future.result())

        # approach 3  (同一个任务, 线程池提交多次同一类任务可以用 map)
        future_list = executor.map(down_images, urls)
        for future in future_list:
            print(future)