data = "{u'8ceb4a9c-818a-4b4e-91bb-bb3b0624cd44': {'status': u'ACCEPTED', 'updated_timestamp': u'2016-02-05T10:58:11.363Z', 'created_timestamp': u'2016-02-05T10:53:59.458Z', 'default_chat_thread_id': u'8ceb4a9c-8182016-02-05-10-58-11-361', 'user_id': u'8ceb4a9c-818a-4b4e-91bb-bb3b0624cd44'}, u'c2bc6da4-2d03-450a-b5e7-e2710ce78543': {'status': u'ACCEPTED', 'updated_timestamp': u'2016-02-12T09:45:49.841Z', 'created_timestamp': u'2016-02-12T09:45:49.729Z', 'default_chat_thread_id': u'4606c4f8-29b2016-02-12-09-45-49-841', 'user_id': u'c2bc6da4-2d03-450a-b5e7-e2710ce78543'}}"
print data

#user_id = data[data.find('user_id')+12:data.find('}',data.find('user_id'))-1]
#user_id = user_id[:-1]
#print user_id
#print type(user_id)
while data.find('user_id')>0:
    user_id = data[data.find('user_id')+12:data.find('}',data.find('user_id'))-1]
    print user_id
    data = data[data.find('user_id')+12:]
