
import glob
import subprocess

testnames = glob.glob("tc_*.txt")
testnames.sort()
expectnames = [] 
for test_name in testnames:
    expect_name = test_name.replace("tc_","expect_")
    expectnames.append(expect_name)

for idx in range(len(testnames)):
    testname = testnames[idx]
    expectname = expectnames[idx]
    ifh = open(testname, "r")
    args = ["python", "solution.py"]
    output = subprocess.check_output(args, stdin = ifh)

    efh = open(expectname, "r")

    print "%s" % (testname),
    if output.strip() == efh.read().strip():
        print "    pass"
    else:
        print "    !!! FAIL !!!"
        output_fn = "%s.run_output" % testname
        ofh = open(output_fn,"w")
        ofh.write(output)
        ofh.close()
        print "run:\n  tkdiff %s %s" % (output_fn, expectname)


