def reader(filehandle):
    first = True

    for line in filehandle:
        line = line.strip('\n').split('\t')

        if first:
            header = {k: v for v, k in enumerate(line)}
            first = False
            continue

        try:
            yield {k: line[v] for k, v in header.items()}
        except IndexError, ex:
            print "Num of columns: ", len(line)
            print line
            pdb.set_trace()
            raise ex
