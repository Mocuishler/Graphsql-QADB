

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

# gcmd = '''run job load_Objective_Clause_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Objective_Clause_test.csv",separator=" ",EOL="\n";run job load_Action_Locative_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Action_Locative_test.csv",separator=" ",EOL="\n";run job load_Action_Manner_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Action_Manner_test.csv",separator=" ",EOL="\n";run job load_Action_Modify_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Action_Modify_test.csv",separator=" ",EOL="\n";run job load_Dative_Action_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Dative_Action_test.csv",separator=" ",EOL="\n";run job load_Field_Attrib_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Field_Attrib_test.csv",separator=" ",EOL="\n";run job load_Agent_Action_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Agent_Action_test.csv",separator=" ",EOL="\n";run job load_Argument_Attrib_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Argument_Attrib_test.csv",separator=" ",EOL="\n";run job load_Patient_Action_test USING FILENAME = "/home/graphsql/cmb_knowledge_graph/file/Patient_Action_test.csv",separator=" ",EOL="\n"'''
#
# data=gcmd.split(";")
# for i in data:
#     tmp = '''gsql "%s"'''%i
#     w = subprocess.Popen(i, shell=True)
#     w.wait()
