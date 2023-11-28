def getNearbyDevices():
    from bluetooth import discover_devices

    while True:
        nearby_devices = len(discover_devices(lookup_names=False))