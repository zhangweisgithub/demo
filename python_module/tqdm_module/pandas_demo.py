# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from tqdm import tqdm


df = pd.DataFrame(np.random.randint(0, 100, (10000000, 6)))
tqdm.pandas(desc="my bar！")
df.progress_apply(lambda x: x ** 2)



