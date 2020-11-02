import pytest
import haeufigkeit

def test_count_occurences():
    input_list = [2,3,4,2,3,3,2,4,3]
    output_expect = {2: 3, 3: 4, 4: 2} 
    
    result = haeufigkeit.count_occurences(input_list)
        
    assert result == output_expect


def test_count_occurences2():      
    data = [
        [[3,4,5,3,4,3], { 3:3, 4:2, 5:1 }],
        [[3,4,5,2,3,4,3], { 2:1, 3:3, 4:2, 5:1 }]
        ]        
        
    for i in data:    
        stat = haeufigkeit.count_occurences(i[0])        
        assert stat == i[1]    