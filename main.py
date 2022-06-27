import pywf as wf


class HttpRequester:
    def __init__(self):
        self.url: list = [
            "http://www.sogou.com",
            "https://www.zhihu.com/people/kedixa",
            "https://fanyi.sogou.com/document"
        ]

    def parallel_callback(self, p):
        print("All series in this parallel is done")

    def http_callback(self, http_task):
        req = http_task.get_req()
        resp = http_task.get_resp()
        print("uri:{} status:{}".format(
            req.get_request_uri(),
            resp.get_status_code()))

    def execute_(self):
        parallel = wf.create_parallel_work(self.parallel_callback)
        for u in self.url:
            task = wf.create_http_task(u, 4, 2, self.http_callback)
            series = wf.create_series_work(task, None)  # without callback
            parallel.add_series(series)
        parallel.start()

        wf.wait_finish()


HttpRequester().execute_()