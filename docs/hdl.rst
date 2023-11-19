Software Communication HDL
==========================


.. mermaid::

    flowchart LR

        subgraph legend [Legend]
            node_hardware[Hardware]
            node_software([Software])
            node_bus{Bus}
        end

        subgraph oresat[CubeSat]

            subgraph c3_card[C3 Card]
                radio1[AX5043 L Band RX]
                radio2[AX5043 UHF TXRX]

                subgraph c3_a8[Octavo A8 running Debian Linux]
                    c3_app([C3 App])
                    ax5043_app([AX5043 App])
                end

                c3_app <--> |Socket IO| ax5043_app
                radio1 --> |SPI| ax5043_app
                radio2 <--> |SPI| ax5043_app
            end

            subgraph gps_card[GPS Card]
                gps_chip1[MAX2771 - SDR GPS receiver]
                gps_chip2[Orion B16 - hardware GPS receiver]

                subgraph gps_a8[Octavo A8 running Debian Linux]
                    gps_app([GPS App])
                    gps_prusdr([PRUsdr MAX2771])
                end

                gps_chip1 --> gps_prusdr
                gps_chip2 --> |Serial| gps_app
                gps_prusdr --> gps_app
            end

            subgraph st_card[Stars Tracker Card]
                st_cam[AR013x Camera]

                subgraph st_a8[Octavo A8 running Debian Linux]
                    st_app([Star Tracker App])
                    st_prucam([PRUcam AR013x])
                end

                st_cam --> st_prucam
                st_prucam --> st_app
            end

            subgraph dxwifi_card[DxWiFi Card]
                dxwifi_cam[UC130MPA Camera]
                dxwifi_tx[AR7201 TX]

                subgraph dxwifi_a8[Octavo A8 running Debian Linux]
                    dxwifi_app([DxWiFi App])
                end

                dxwifi_cam --> |Serial| dxwifi_app
                dxwifi_app --> dxwifi_tx
            end

            subgraph cfc_sensor_card[CFC Sensor Card]
                cfc_cam[PIRT 1280 Image Sensor]
            end

            subgraph cfc_card[CFC Card]
                subgraph cfc_a8[Octavo A8 running Debian Linux]
                    cfc_app([CFC App])
                    cfc_prucam([PRUcam PIRT1280])
                end

                cfc_cam --> cfc_prucam
                cfc_prucam --> cfc_app
            end

            subgraph solar_card[Solar Cards x6]
                solar_panel[Solar Panels]
                solar_chip[INA226]

                subgraph  solar_stm[STM32 F0]
                    solar_app([ChibiOS + Solar App])
                end

                solar_panel --> solar_chip
                solar_chip --> |I2C| solar_app
            end

            subgraph  rw_asm[Reaction Wheels x4]
                rw[Reactio Wheel]

                subgraph  rw_stm[STM32 G4]
                    rw_app([ChibiOS + RW App])
                end

                rw_app --> |PWM| rw
            end

            subgraph acs_card[ACS Card]
                imu[BMI088 - IMU]

                subgraph  acs_stm[STM32 F0]
                    acs_app([ChibiOS + IMU App])
                end

                acs_app --> |I2C| imu
            end

            subgraph bat_card[Battery Card]
                subgraph  bat_pack[Battery Pack x2]
                    bat_cell[Battery Cell x2]
                end
                
                bat_chip[MAX17205]

                subgraph  bat_stm[STM32 F0]
                    bat_app([ChibiOS + Battery App])
                end

                bat_pack --> bat_chip
                bat_chip --> |I2C| bat_app
            end

            bus{CAN Bus}

            bus <--> c3_app
            bus <--> gps_app
            bus <--> st_app
            bus <--> dxwifi_app
            bus <--> cfc_app
            bus <--> solar_app
            bus <--> acs_app
            bus <--> bat_app
            bus <--> rw_app
        end

        subgraph GroundStation [UniClOGS]
            direction LR
            gnu([GNURadio])
            server1([Yamcs])

            band1[L band HackRF SDR TX]
            band2[UHF HackRF SDR TX]
            band3[RTL-SDFL SDR RX]
            band4[RTL-SDL SDR RX]

            server1 <--> |Socket IO| gnu

            gnu <--> band1
            gnu <--> band2
            gnu <--> band3
            gnu <--> band4

        end

        band1 -.-> |EDL Up L Band| radio1
        band2 -.-> |EDL Up UHF| radio2
        radio2 -.-> |EDL Down| band3
        radio2 -.-> |UHF Beacon Down| band4
