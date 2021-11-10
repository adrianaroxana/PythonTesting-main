class ProtectedSource:
    def _internal_logger(self):
        print("protected method")


function_call = ProtectedSource()
function_call._internal_logger()