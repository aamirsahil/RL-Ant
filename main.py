from system import System

def main():
    data = {
        "total_time" : 50000,
        "agent_no" : 10,
        "world_data" : {
            "width" : 20,
            "height" : 20,
            "boundary" : "reflective",
            "evoporate" : True,
            "disperse" : True,
            "evoporation_rate" : 0.99,
            "dispersion_rate" : 0.04
        },
    }
    system = System(**data)
    system.load()
    system.run()
    print("done")
if __name__ == "__main__":
    main()