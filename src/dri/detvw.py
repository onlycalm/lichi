##
# @file detvw.py
# @brief 检测可视化模块。
# @details 无
# @author Calm
# @date 2021-09-08
# @version v1.0.0
# @copyright Calm
#

from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem

##
# @class cDetVw
# @brief 检测浏览控件。
# @details 基于tableWidget控件，浏览检测记录。
# @note 无
# @attention 无
#
class cDetVw:
    ##
    # @brief 构造函数。
    # @details 无
    # @param self 对象指针。
    # @param Obj 指向已有对象。
    # @return 无
    # @note 无
    # @attention 无
    #
    def __init__(self, Obj = None):
        if Obj:
            self.Tw = Obj
        else:
            self.Tw = QTreeWidget()

    ##
    # @brief 添加一条检测记录。
    # @details 往DetVw控件中添加一条检测记录。
    # @param self 对象指针。
    # @param Rec 类型为列表，一条Det记录。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ApdRec(self, Rec):
        self.Tw.addTopLevelItem(QTreeWidgetItem(Rec)) #添加一项

    ##
    # @brief 清空Det记录。
    # @details 无
    # @param self 对象指针。
    # @return 无
    # @note 无
    # @attention 无
    #
    def ClrDet(self):
        self.Tw.clear()
