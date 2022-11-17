# 1) same process 2)number of times /reach the result


# sum of the elements in list
li = [23, 34, 45, 44, 25, 66]

# print(li[0])
length = len(li)
print(length)
print(range(length))
# 18  times will take the iterations
index_res = 0
for item in range(length):
    if item % 2 == 1:
        index_res = index_res + li[item]
    print(index_res)

# 6 times will take the iterations
#data_res = 0
#for item in li:
 #   if item % 2 == 0:
 #       data_res = data_res + item

#print(data_res)

# print("acd".count)
# print(enumerate(li))
#enum_res = 0

# 6 iterations ,but waste of memory (because it will give the both index values and data)

#for index, item in enumerate(li):
  #  if index % 2 == 0:
 #       enum_res = enum_res + item
#        print(enum_res)

data=[
{
    "env": "QA",
   "event_type": "evt",
    "game_name": "AStats_IOS_QA",
    "i": "SDK_STANDARD",
    "json_data": {
        "bootTimeKernNano": 1666367804118225,
        "conn_type": "Wifi",
        "deviceBootTimeSec": 1666367797,
        "encrypted": "1",
        "idfa": "00000000-0000-0000-0000-000000000000",
        "idfv": "659B54B0-6D6B-4EF0-9E80-E99679A80379",
        "monotonicRaw": 14042,
        "opt_out": "1",
        "realtime": 1666381839
    }
}]


print(data)



#data=["idfa":]
print(data[0]["json_data"]["idfa"])

data2=[
  {
    "env": "QA",
    "event_type": "evt",
    "game_name": "AStats_IOS_QA",
    "i": "SDK_STANDARD",
    "json_data": {
      "bootTimeKernNano": 1666367804118225,
      "conn_type": "Wifi",
      "deviceBootTimeSec": 1666367797,
      "encrypted": "1",
      "idfa": "00000000-0000-0000-0000-000000000000",
      "idfv": "659B54B0-6D6B-4EF0-9E80-E99679A80379",
      "monotonicRaw": 14042,
      "opt_out": "1",
      "realtime": 1666381839
    },
    "kt_v": "6.1.0-e78b689",
    "revid": "IDFV-D1AB2A53-C348-43AC-83DC-4A14CA70A747_1666381839",
    "s": "IDFV-D1AB2A53-C348-43AC-83DC-4A14CA70A747",
    "st1": "APP",
    "st2": "SESSION_START",
    "ts": 1666381839,
    "v_maj": "2022.7.0",
    "v_min": "2115"
  },
  {
    "env": "QA",
    "event_type": "evt",
    "game_name": "AStats_IOS_QA",
    "i": "SDK_STANDARD",
    "json_data": {
      "RevSDKVersion": "2022.7.0",
      "version": "5.2.0-b5a284d"
    },
    "kt_v": "6.1.0-e78b689",
    "l": 0,
    "revid": "IDFV-D1AB2A53-C348-43AC-83DC-4A14CA70A747_1666381839",
    "s": "IDFV-D1AB2A53-C348-43AC-83DC-4A14CA70A747",
    "sess_id": "d4715da0-ba77-4741-ad01-893ce962403c",
    "st1": "SDK",
    "st2": "SDK_VERSION",
    "st3": "GluAds",
    "ts": 1666381839,
    "v": 0,
    "v_maj": "2022.7.0",
    "v_min": "2115"
  }
]

