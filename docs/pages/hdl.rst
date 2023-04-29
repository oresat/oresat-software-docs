Software Communication HDL
==========================


.. mermaid::

    flowchart LR
        subgraph legend [Legend]
            node_hardware[Hardware]
            node_software([Software])
        end

        bus([CAN Bus])

        subgraph GroundStation [UniCLOGs]
            direction LR
            gnu[Gnu-Radio]
            server1([Yamcs])

            band1[L band HackRF SDR TX]
            band2[UHF HackRF SDR TX]
            band3[RTL-SDFL SDR RX]
            band4[RTL-SDL SDR RX]

            server1 <--> |Socket 10| gnu

            gnu <--> band1
            gnu <--> band2
            gnu <--> band3
            gnu <--> band4

        end

        subgraph controller[C3]
            subgraph c_a8[A8]
                app1[Oresat C3 Software]
                c3_olaf[OLAF]
                c3_os[Debian Linux]
            end

            chip1[AX5043 L Band RX]
            chip2[AX5043 UHF TXRX]

            app1 <--> chip1
            app1 <--> chip2

            app1 <--> c3_olaf <--> c3_os
        end

        band1 -->|EDL Up L Band| chip1
        band2 -->|EDL Up UHF| chip2
        chip2 -->|EDL Down| band3
        chip2 --> |UHF Beacon Down| band4

        subgraph oresat[CubeSat]
            subgraph card1[GPS]
                subgraph a8[A8]
                    app3([Oresat GPS])
                    gps_olaf([OLAF])
                    gps_os([Debian Linux])

                    app3 <--> gps_olaf
                    gps_olaf <--> gps_os
                end
                gps_hardware1([MAX2771])
                gps_hardward2([Orion B16])
            end

            gps_olaf --> bus
            gps_hardware1 --> |PRU| app3
            gps_hardward2 --> |Serial| app3

            subgraph card2[Stars Tracker]
                chip4[AR013x Camera]

                subgraph st_card[Star Tracker Card]
                    st_app([openstartracker.org])
                    app4([Oresat-star-tracker])
                    st_olaf([OLAF])
                    st_os([Debian Linux])
                    app5[PRU can]
                end

                chip4 --> st_card
            end

            app4 <--> st_olaf
            st_os <--> st_olaf
            st_app <--> app4
            app5 --> app4


            subgraph card3[dxwifi]
                app6([Oresat dxwifi])
                chip5[USB Camera]
                chip6[TX Chip]

                app6-->chip5
                app6-->chip6
            end

            subgraph card4[CFC]
                app7([Oresat-CFC])
                app8[PRU can]
                chip7[PIRT 1280 Camera]
            end

            app7-->app8---chip7

            chip8[Solar x8]
            chip9[Imu]
            chip10[Battery x2]


        end

        bus <--> c3_olaf
        bus<-->gps_olaf
        bus <--> st_olaf
        bus<-->app6
        bus<-->app7
        bus<-->chip8
        bus<-->chip9
        bus<-->chip10

