from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler

def base_exception_handler(exc, context):
    response = exception_handler(exc, context)

    sample={}

    # check that a ValidationError exception is raised
    if isinstance(exc, ValidationError):

    # here prepare the 'custom_error_response' and
    # set the custom response data on response object
        print(type(response.data))

        #response.data can be of list type ,so.....
        if isinstance(response.data,list):
            sample["detail"]=response.data[0]#get first message from list,example is given below:
            response.data=sample

        else:

            if response.data.get("detail",None):

                sample["detail"]=response.data["detail"][0]
                response.data=sample

            elif response.data.get("name", None):

                sample["detail"]=response.data["name"][0]
                response.data=sample

            elif response.data.get("description", None):

                sample["detail"] = response.data["description"][0]
                response.data=sample

            elif response.data.get("start_date",None):

                sample["detail"] = response.data["start_date"][0]
                response.data=sample

            elif response.data.get("end_date",None):

                sample["detail"] = response.data["end_date"][0]
                response.data=sample

            elif response.data.get("status",None):

                sample["detail"] = response.data["status"][0]
                response.data=sample

            elif response.data.get("username",None):

                sample["detail"] = response.data["username"][0]
                response.data=sample

                
             
        
    
    print("response",response)
    
    return response

"""
example:
{
    "error1",
    "error2",
    ......
    "errorn
}
retrieve first error as next error will be raised automatically when user corrects first one
"""