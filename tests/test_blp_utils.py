#  -*- coding: utf-8 -*-
# @author: zhangping

from src.fdutils.blp_utils import BlpUtil


def test_blp_utils():
    d = BlpUtil.bdh('600570 CH Equity', flds='PX_LAST', start_date='2021-04-01',
                    overrides={'Currency': 'USD'})
    print(d)


if __name__ == '__main__':
    test_blp_utils()
