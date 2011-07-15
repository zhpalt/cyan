l = [3, 4, 5]
end = {'end':'[END]\n'}
print l, end
print '%s %s' % (*l, **end)
