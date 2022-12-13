import Lesson_7.Dop_Moduls.view
import Lesson_7.Dop_Moduls.guid
import Lesson_7.Dop_Moduls.logger

def button_click():
    from Lesson_7.Dop_Moduls import view
    value_a = view.get_value()
    oper = view.get_operator()
    value_b = view.get_value()

    from Lesson_7.Dop_Moduls import guid
    func = guid.dict_ar[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)
    from Lesson_7.Dop_Moduls import logger
    logger.get_log(result, oper, value_a, value_b)