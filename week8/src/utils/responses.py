class CommonResponses:

    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_204_NO_CONTENT = 204

    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_404_NOT_FOUND = 404

    @classmethod
    def ok_200(cls, data=None):

        data_content = {
            'message': "Success",
            'status': 'HTTP_200_OK',
            'data': data,
        }
        return data_content, cls.HTTP_200_OK

    @classmethod
    def created_201(cls, data=None):

        data_content = {
            'message': "The object has been created",
            'status': 'HTTP_201_CREATED',
            'data': data,
        }
        return data_content, cls.HTTP_201_CREATED

    @classmethod
    def no_content_204(cls):

        data_content = {
            'message': "Object deleted!",
            'status': 'HTTP_204_NO_CONTENT',
        }
        return data_content, cls.HTTP_204_NO_CONTENT

    @classmethod
    def bad_request_400(cls, data=None):

        data_content = {
            'message': "Some fields are not valid, please check the data for errors",  # noqa: E501
            'status': 'HTTP_400_BAD_REQUEST',
            'data': data,
        }
        return data_content, cls.HTTP_400_BAD_REQUEST

    @classmethod
    def unauthorized_401(cls, data=None):

        data_content = {
            'message': "Invalid authentication credentials for the requested resource.",  # noqa: E501
            'status': 'HTTP_401_UNAUTHORIZED',
            'data': data,
        }
        return data_content, cls.HTTP_401_UNAUTHORIZED

    @classmethod
    def not_found_404(cls):

        data_content = {
            'message': "The object you requested doesn't exist",
            'status': 'HTTP_404_NOT_FOUND',
        }
        return data_content, cls.HTTP_404_NOT_FOUND
