from flask_restplus import fields


class TimeDeltaFormat(fields.Raw):
    def format(self, value):
        return str(value)


class JsonFormat(fields.Raw):
    def format(self, value):
        return value
