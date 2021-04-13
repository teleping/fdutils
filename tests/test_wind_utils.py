#  -*- coding: utf-8 -*-
# @author: zhangping

from src.fdutils import WindUtil


def test_wind_utils():
    d = WindUtil.tdays(start_date='2021-01-01')
    print(d)

    d = WindUtil.sectors('1000010084000000', date='2020-08-28')
    print(d)

    d = WindUtil.sectors_by_code('APFI.WI', date='2020-08-28')
    print(d)

    d = WindUtil.fu_contracts('A.DCE')
    print(d)

    d = WindUtil.fu_hiscode('A.DCE', '2020-01-01')
    print(d)

    d = WindUtil.wsd('600570.SH', 'open,close,high,low')
    print(d)

    d = WindUtil.wsd('600570.SH', 'open,close,high,low', start_date='2021-04-01', end_date='2021-04-05', options='')
    print(d)

    d = WindUtil.edb('M0000185')
    print(d)

    d = WindUtil.edb('M0000185', start_date='2020-01-01', end_date='2021-04-01', options='')
    print(d)


if __name__ == '__main__':
    test_wind_utils()
