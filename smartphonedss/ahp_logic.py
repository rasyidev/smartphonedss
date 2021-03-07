import numpy as np
class AHP:
    # RI = Random Concistency Index
    RI = (0, 0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.59)

    def __init__(self, obj, criteria_count):
        self.obj = obj
        self.criteria_count = criteria_count
        
#     create pairwise comparison matrix
    def create_pcm(self):
      result_object = {
         'performance_vs_price': {'addr': (0,1), 'value':  self.obj['performance_vs_price']},
         'performance_vs_camera': {'addr': (0,2), 'value': self.obj['performance_vs_camera']},
         'performance_vs_memory': {'addr': (0,3), 'value':  self.obj['performance_vs_memory']},
         'performance_vs_battery': {'addr': (0,4), 'value':  self.obj['performance_vs_battery']},
         'performance_vs_reputation': {'addr': (0,5), 'value': self.obj['performance_vs_reputation']},
         'price_vs_camera': {'addr': (1,2), 'value': self.obj['price_vs_camera']},
         'price_vs_memory': {'addr': (1,3), 'value': self.obj['price_vs_memory']},
         'price_vs_battery': {'addr': (1,4), 'value': self.obj['price_vs_battery']},
         'price_vs_reputation': {'addr': (1,5), 'value': self.obj['price_vs_reputation']},
         'camera_vs_memory': {'addr': (2,3), 'value': self.obj['camera_vs_memory']},
         'camera_vs_battery': {'addr': (2,4), 'value':  self.obj['camera_vs_battery']},
         'camera_vs_reputation': {'addr': (2,5), 'value':  self.obj['camera_vs_reputation']},
         'memory_vs_battery': {'addr': (3,4), 'value': self.obj['memory_vs_battery']},
         'memory_vs_reputation': {'addr': (3,5), 'value': self.obj['memory_vs_reputation']},
         'battery_vs_reputation': {'addr': (4,5), 'value': self.obj['battery_vs_reputation']},
      }
#     create matrix 6x6 with default values of 1
      pcm = np.ones((self.criteria_count, self.criteria_count))
      for item in result_object:
         addr = result_object[item]['addr']
         mirror_addr = addr[::-1]
         value = int(result_object[item]['value'][0])
         # print('a', addr, result_object[item]['value'][0])
         if value > 0:
               pcm[addr] = value
               pcm[mirror_addr] = 1/value
         else:
               value = value * -1
               pcm[mirror_addr] = value
               pcm[addr] = 1/value
      return pcm
    
    def get_normalized_pcm(self):
        pcm = self.create_pcm()
        col_sum = []
        for i in range(self.criteria_count):
            col_sum.append(sum(pcm[:,i]))
        
        normalized_pcm = np.ones((6,6))
        for i in range(self.criteria_count):
            for j in range(self.criteria_count):
                normalized_pcm[i][j] = pcm[i][j] / col_sum[j]
        return normalized_pcm
    
    def get_criteria_weight(self):
        normalized_pcm = self.get_normalized_pcm()
        normalized_pcm_row_avg = []
        for i in range(self.criteria_count):
            normalized_pcm_row_avg.append(sum(normalized_pcm[i])/self.criteria_count)
        return normalized_pcm_row_avg
    
    def generate_cr_matrix(self):
        pcm = self.create_pcm()
        normalized_pcm = self.get_normalized_pcm()
        normalized_pcm_row_avg = []
        for i in range(self.criteria_count):
            normalized_pcm_row_avg.append(sum(normalized_pcm[i])/self.criteria_count)
            
        cr_matrix = np.ones((self.criteria_count,self.criteria_count))
        for i in range(self.criteria_count):
            for j in range(self.criteria_count):
                cr_matrix[i][j] = pcm[i][j] * normalized_pcm_row_avg[j]
        return cr_matrix
    
    def is_consistent(self):
        cr_matrix = self.generate_cr_matrix()
        total_criteria_weight = []
        for i in range(self.criteria_count):
            total_criteria_weight.append(sum(cr_matrix[i]) / self.criteria_count)
        
        criteria_weight = self.get_criteria_weight()
        lambda_max = np.array(total_criteria_weight) / np.array(criteria_weight)
        print(lambda_max)
        RI = (sum(lambda_max) - self.criteria_count) / (self.criteria_count-1)
        # Consistency Ratio
        CR = RI / self.RI[self.criteria_count]
        return CR < 0.1
    