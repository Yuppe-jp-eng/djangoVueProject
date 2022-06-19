from backend.lib.enum import BookingModelStatus


def my_context_processor(req):
    return {
        "BookingModelStatus": BookingModelStatus,
        "COMPLETE_STATUS": BookingModelStatus.COMPLETE.key,
        "AWAIT_STATUS": BookingModelStatus.AWAIT.key,
        "TEMP_STATUS": BookingModelStatus.TEMP.key,
        "CANCEL_STATUS": BookingModelStatus.CANCEL.key,
    }
