#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

cmd = "gsql load_AA_Objective_Clause_test.gsql;gsql load_Action_Locative_test.gsql;gsql load_Action_Manner_test.gsql;gsql load_Action_Modify_test.gsql;gsql load_Dative_Action_test.gsql;gsql load_Field_Attrib_test.gsql;gsql load_OA_Agent_Action_test.gsql;gsql load_OO_Argument_Attrib_test.gsql;gsql load_Patient_Action_test.gsql;gsql load_OA_Object_Complement_test.gsql;"

new = cmd.split(";")
for i in new:
    p = subprocess.Popen(i, shell=True)
    p.wait()

print
print "Load complete"
print
