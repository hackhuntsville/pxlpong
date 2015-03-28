import alphasign

def main():
  sign = alphasign.Serial(device="/dev/ttyUSB0")
  sign.connect()
  sign.clear_memory()
  return #if you are just clearing the sign's memory this is enough.

#  sign.beep(   duration=0.8,
#               frequency=250, #anything above 0 just means the same freq on our sign
#               repeat=0) #that is, do not repeat - just do it once

  t = "Hack Huntsville"

  normal_state = alphasign.Text(        label="A",
                                        data=t,
                                        size=192,
                                        mode=alphasign.modes.HOLD,
                                        position=alphasign.positions.FILL)

  # allocate memory for these objects on the sign
  sign.allocate((normal_state,))

  # tell sign to only display the counter text
  sign.set_run_sequence((normal_state,))

  # write objects
  for obj in (normal_state,):
    sign.write(obj)

if __name__ == "__main__":
  main()

