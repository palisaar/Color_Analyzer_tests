name = "test"
f = open("L:\Studium\NEB\Color Analyzer\CA tests\\" + name + ".txt", "w")   # 'r' for reading and 'w' for writing
f.write("Hello World from " + f.name)    # Write inside file
f.close()                                # Close file