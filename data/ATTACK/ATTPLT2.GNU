#Command file for plotting snail attack data
set title "Reactive Distance to Mechanical Stimulus"
set xlabel "Distance from P. conicus (mm)"
set ylabel "No. of Responses"
plot [0:50] [0:12] "attack3" title 'Attack only' w linesp, \
	"attack4" title 'Other response' w linesp, \
	"attack1" title 'All responses' w linesp

