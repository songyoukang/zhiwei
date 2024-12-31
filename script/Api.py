import requests
class MyApi():
        def get_task(self):
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNjU0MDI0MTgxMDczNTM5MTc4Iiwicm5TdHIiOiIxUkRtcGUxdW1YQlVqbTh4THZVU1RRSkdpUzVtMmJjMyIsInVzZXJJZCI6MTY1NDAyNDE4MTA3MzUzOTE3OH0.FkX48CYVc1YUfLYkR9VURiXTuetVkw19b_ySQRUqXdc'
            url = 'http://10.10.200.104:28115/security-api/workflow/task/homeStatistics'
            header = {'Authorization': f'{token}',
                      'Content-Type': 'application/json'}
            res = requests.get(url=url, headers=header)
            return res.json()


        def bb(self):
            token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpblR5cGUiOiJsb2dpbiIsImxvZ2luSWQiOiJzeXNfdXNlcjoxNjU0MDI0MTgxMDczNTM5MTc4Iiwicm5TdHIiOiJuTFVpamVzRk9acVJZdmxBSTQzMFowSndjTExNdjlMQiIsInVzZXJJZCI6MTY1NDAyNDE4MTA3MzUzOTE3OH0.MOzcXcuiyLF-roAvdpANsI3TcBIy9KioyWpLFknm8q0'
            url = 'http://10.10.200.104:28115/security-api/workflow/task/homeStatistics'
            header = {'Authorization': f'{token}',
                      'Content-Type': 'application/json'}
            res1 = requests.get(url=url, headers=header)
            return res1.json()
