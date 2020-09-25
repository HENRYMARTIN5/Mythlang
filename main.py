# Myth compiler V1.1.0
import compiler
filetype = "standard/.mth"
runner = compiler.MythCompiler(filetype)
runner.Run("tests.mth", 'debug')