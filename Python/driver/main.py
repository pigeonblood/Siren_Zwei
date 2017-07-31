#-*-coding:utf-8;-*-
#importing modules
import sys
sys.path.append("../framework")
import moduleLoader as ml

#internal modules into dictionary
#対象ディレクトリのモジュールをすべて自動的に読み込み
#モジュールへのアクセス方法: mod[<モジュール名>]
mod = ml.LoadModules()
