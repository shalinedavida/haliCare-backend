class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = "__all__"

    def create(self, validated_data):
        address = validated_data.get("address", "")
        if address:
            lat, lon = geocode_address(address)
            validated_data["latitude"] = lat
            validated_data["longitude"] = lon
        return super().create(validated_data)
