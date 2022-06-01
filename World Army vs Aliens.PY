World Army vs Aliens (100 Marks)
The world is going to be attacked by the aliens. The space intelligence department has raised an alarm and the world armies are coming together to fight them. The planning and strategizing is being done to make the maximum impact on the alien ships. The deadly missiles are to be put into action. The missiles are targeted to destroy the alien ships in space and disable them to land on the Earth.


The army is planning to launch the attack at A time (hh mm) to get an advantage. For each attack, they know the time the missile will require to hit the coming alien ship. They all are busy in preparation and want to know the time at which the blast will occur and the alien ship will be destroyed in pieces. Can you find the time of the blast ?


Note: The World Army follows a 24-hour time format and you need to find the time of blast accordingly. The time will be in the hh mm format.


Example:





Input Format
The first line of input consists of the launch time in hh mm format separated by space.

The second line of input consists of the travel time for the missile in hh mm format separated by space.



Constraints
00<= hh <=23

00<= mm <=59



Output Format
Print the time at which the blast will occur and the spaceship will be destroyed.











DT_HH,DT_MM = input().split(" ")
TT_HH,TT_MM = input().split(" ")
DT_HH = int(DT_HH)
DT_MM = int(DT_MM)
TT_HH = int(TT_HH)
TT_MM = int(TT_MM)

total_minutes_of_travel = (TT_HH * 60) + TT_MM

for x in range(1, total_minutes_of_travel+1):
    DT_MM += 1
    if (DT_MM == 60):
        DT_MM = 0
        DT_HH += 1
        if (DT_HH == 24):
            DT_HH = 0

print(f"{DT_HH:02d}", f"{DT_MM:02d}")
